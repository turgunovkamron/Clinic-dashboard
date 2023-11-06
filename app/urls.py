from django.urls import path

from .services.auth import sign_in, sign_up, sign_out, er, profile_edit
from .services.auto import gets, auto_form, auto_del
from .services.client import client_doc
from .services.direc import list_members, banner, grader, spammer
from .views import index, contact

urlpatterns = [
    path("", index, name="home"),

    # auth
    path("auth/login/", sign_in, name="sign_in"),
    path("auth/regis/", sign_up, name="regis"),
    path("auth/logout/", sign_out, name="sign_out"),
    # path("auth/profile/", profile, name="profile"),
    path("edit", profile_edit, name="profile_edit"),
    path("auth/contacts/" , contact , name="contacts"),


    # auto
    path("auto/<key>/", gets, name="dashboard-auto-list"),
    path("auto/<key>/detail/<int:pk>/", gets, name="dashboard-auto-detail"),
    path("auto/<key>/add/", auto_form, name="dashboard-auto-add"),
    path("auto/<key>/edit/<int:pk>/", auto_form, name="dashboard-auto-edit"),
    path("auto/<key>/del/<int:pk>/", auto_del, name="dashboard-auto-delete"),

    path("member/<int:type>/", list_members, name="members"),
    path("member/new/<int:new>/", list_members, name="members-new"),
    path("grader/<int:pk>/<int:ut>/<int:dut>/", grader, name="grader"),
    path("banner/u-<int:user_id>/<int:type>/<int:status>/", banner, name="banner"),
    path("error/404.html/", er, name="404.html"),
    path("spam/<int:pk>/<int:dut>/", spammer, name="spammer"),

    # client
    path("client/doc/<int:service>/", client_doc, name="client_doc")

]
