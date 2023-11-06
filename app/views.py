from contextlib import closing

from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render
from methodism import dictfetchall, dictfetchone

from app.models import Service


# Create your views here.
@login_required(login_url="sign_in")
def index(requests):
    sql = "select id , name , familya , phone from app_user where new=true and not ut = 1 limit 3"
    cnt = "SELECT COUNT(*) as cnt from app_user WHERE new=TRUE and not ut = 1"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)

    with closing(connection.cursor()) as cursor:
        cursor.execute(cnt)
        cnt_result = dictfetchone(cursor)

    service = Service.objects.all()
    ctx = {
        "notifs": result,
        "cntt": cnt_result,
        "service": service
    }
    return render(requests, "page/index.html", ctx)


@login_required(login_url="sign_in")
def contact(requests):
    ctx = {
        "contact": contact
    }
    return render(requests, "contacts.html", ctx)
