import datetime
from contextlib import closing

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import connection, models
from django.shortcuts import render, redirect
from methodism import dictfetchall, dictfetchone

from app.models import User
from app.models.doctor import Spam


def list_members(request, type=None, new=False):
    kwargs = {"ut": type} if type else {}
    if request.user.ut != 1:
        return redirect("home")
    if new:
        kwargs['new'] = new

    sql = "select id , name , familya , phone from app_user where new=true and not ut = 1 limit 3"
    cnt = "SELECT COUNT(*) as cnt from app_user WHERE new=TRUE and not ut = 1"

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)

    with closing(connection.cursor()) as cursor:
        cursor.execute(cnt)
        cnt_result = dictfetchone(cursor)

    pagination = User.objects.filter(**kwargs).order_by("-pk")
    paginator = Paginator(pagination, settings.PAGINATE_BY)
    page_number = request.GET.get("page", 1)
    paginated = paginator.get_page(page_number)

    uzunlik = len(paginated) // settings.PAGINATE_BY
    if len(pagination) % settings.PAGINATE_BY:
        uzunlik += 1
    length = [x for x in range(1, uzunlik + 1)]

    types = {
        2: "admin",
        3: "doctor",
        4: "member",
    }
    print(length, page_number)

    ctx = {
        "roots": paginated,
        "root_type": types.get(type, 'New'),
        "notifs": result,
        "cntt": cnt_result,
        "page_len": length,
        "current_page": int(page_number)
    }

    return render(request, "page/members.html", ctx)


@login_required(login_url='sign-in')
def banner(request, user_id, type, status=False):
    if request.user.ut != 1:
        return redirect("home")
    try:
        user = User.objects.filter(id=user_id).first()
        user.is_active = status
        user.new = False
        user.save()
    except:
        pass

    return redirect('members', type=type)


@login_required(login_url='sign-in')
def grader(request, pk, ut, dut):
    if request.user.ut != 1:
        return redirect("home")
    try:
        user = User.objects.filter(id=pk).first()
        user.ut = ut
        user.new = False
        user.save()
    except:
        pass

    return redirect('members', type=dut)


@login_required(login_url='sign-in')
def spammer(request, pk, dut):
    if request.user.ut != 1:
        return redirect('home')
    # try:
    user = User.objects.filter(id=pk).first()
    Spam.objects.create(user=user)
    user.is_spam = True
    user.save()
    # except:
    #     pass
    return redirect('members', type=dut)
