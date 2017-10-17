from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
	url(r'^$', Index),
    url(r'^pre_registro_egresado/',PreRegisterGraduated, name="graduated_registration"),
    url(r'^pre_registro_admin/',PreRegisterAdmin, name="admin_registration"),
    url(r'^login_egresado/',LoginEgresado, name="login_egresado"),
    url(r'^new_password/',NewPassword, name="new_password"),
    url(r'^login_admin/',LoginAdmin, name="login_admin"),
    url(r'^dashboard_admin/',DashboardAdmin, name="dashboard_admin"),
    url(r'^dashboard_egresado/',DashboardEgresado, name="dashboard_egresado"),
    url(r'^logout/',closeSession, name="logout"),

]