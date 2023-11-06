import datetime
from contextlib import closing

from django.conf import settings
from django.contrib.auth import logout
from django.db import connection
from django.shortcuts import redirect
from methodism import dictfetchone

from app.models.doctor import Spam


def ut(requests):
    try:
        if not requests.user.is_active:
            logout(requests)
            return redirect("login")
        types = {
            1: "page/direc/main.html",
            2: "page/admin/main.html",
            4: "page/client/main.html",
            3: "page/doc/main.html",

        }.get(requests.user.ut, "page/client/main.html")
    except:
        types = "page/client/main.html"
    ctx = {"type": types,
           "app_name": settings.APP_NAME,
           "sql_img_url": "http://127.0.0.1:8000/media/"
           }

    if not requests.user.is_anonymous:
        ctx.update({"ut": requests.user.ut})
    return ctx


def check_spam(request):
    spam_user = Spam.objects.filter(user_id=request.user.id, active=True).first()
    if spam_user:
        now = datetime.datetime.now()
        interval = (now - spam_user.date).total_seconds()

        if interval > 0:
            spam_user.active = False
            spam_user.save()

            request.user.is_spam = False
            request.user.save()

            return {'spam': False, 'spam_user': {}}
        return {'spam': True, 'spam_user': spam_user}
    return {'spam': False, 'spam_user': {}}


def count(request):
    sql = """
    select (select count (*) from app_user where ut = 3 ) as cnt_doc ,
    (select count (*) from app_user where ut = 2 ) as cnt_admin ,
    (select count (*) from app_user where ut = 4 ) as cnt_client ,
    (select count(*) from app_service ) as cnt_service 

    from django_session limit 1
    """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dictfetchone(cursor)

    return {
        "count": result

    }
