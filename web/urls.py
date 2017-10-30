from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
	url(r'^$', Index),
    url(r'^pre_registro_egresado/',PreRegisterGraduated, name="graduated_registration"),
    url(r'^pre_registro_admin/',PreRegisterAdmin, name="admin_registration"),
    url(r'^login_egresado/',LoginEgresado, name="login_egresado"),
    url(r'^new_passwordg/',NewPasswordG, name="new_passwordg"),
    url(r'^new_passworda/',NewPasswordA, name="new_passworda"),
    url(r'^login_admin/',LoginAdmin, name="login_admin"),
    url(r'^dashboard_admin/',DashboardAdmin, name="dashboard_admin"),
    url(r'^aceptar_cuentas/',AceptarCuentas, name="aceptar_cuentas"),
    url(r'^dashboard_egresado/',DashboardEgresado, name="dashboard_egresado"), 
    url(r'^dashboard_root/',DashboardRoot, name="dashboard_root"),
    url(r'^aceptar_cuentas_admin/',AceptarCuentasAdmin, name="aceptar_cuentas_admin"),
    url(r'^logout/',closeSession, name="logout"),

]