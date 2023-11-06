import random

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.models.auth import User
from methodism import code_decoder, exception_data

from app.services.forms.forms import UserForms


def sign_in(request):
    if not request.user.is_anonymous:
        return redirect("home")
    ctx = {

    }

    if request.POST:
        password = request.POST.get('pass')
        phone = request.POST.get('phone')

        user = User.objects.filter(phone=phone).first()
        if not user:
            ctx["error"] = "Wrong user or password"
            ctx['etype'] = "phone"
            return render(request, 'page/auth/login.html', ctx)

        if not user.is_active:
            ctx["error"] = "Uzur user ban qilingan "
            ctx['etype'] = 'ban'

        if not user.check_password(password):
            ctx["error"] = "Wrong password"
            ctx['etype'] = 'pass'
            return render(request, 'page/auth/login.html', ctx)
        login(request, user)
        return redirect('home')
    return render(request, 'page/auth/login.html')


def sign_up(request):
    ctx = {

    }
    if request.POST:
        password = request.POST.get('pass')
        phone = request.POST.get('phone')
        pass_c = request.POST.get('pasc')
        gender = int(request.POST.get('gender'))

        user = User.objects.filter(phone=phone).first()
        if user:
            ctx["error"] = "Bunday user bor"
            return render(request, 'page/auth/regis.html', ctx)
        if "terms" not in request.POST:
            ctx["error"] = "Oferta majburiy"
            return render(request, 'page/auth/regis.html', ctx)
        if password != pass_c:
            ctx["error"] = "Parollar bir xil emas "
            return render(request, 'page/auth/regis.html', ctx)
        user = User.objects.create_user(phone=phone,
                                        email=request.POST.get("email"),
                                        password=password,
                                        name=request.POST.get("name"),
                                        gender=gender)

        authenticate(request)
        login(request, user)
        return redirect("home")
    return render(request, 'page/auth/regis.html')


@login_required(login_url="sign_in")
def sign_out(request):
    logout(request)
    return redirect("sign_in")






def er(request):
    ctx = {

    }
    return render(request, '404.html', ctx)


def profile_edit(request):
    user = request.user
    if user.is_anonymous:
        return redirect("sign_in")

    if request.POST:
        user = request.user
        forms = UserForms(request.POST,  instance=request.user)
        if forms.is_valid():
            forms.save()

        else:
            print(forms.errors)
            print("ssssssssssssssssssssss")

    ctx = {
        "user": user
    }

    return render(request, "page/auth/profile_edit.html", ctx)

