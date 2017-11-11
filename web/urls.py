from django.conf.urls import url , include
from django.contrib import admin
from django.contrib.auth import views as auth_views 
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', Index),
    
    url(regex= r'^pre_registro_egresado/$',
        view=PreRegisterGraduated, 
        name="graduated_registration"),
    
    url(regex=r'^pre_registro_admin/$',
        view=PreRegisterAdmin, 
        name="admin_registration"),
    
    url(regex=r'^login_egresado/$',
        view=LoginEgresado, 
        name="login_egresado"),
    
    url(regex=r'^new_passwordg/$',
        view=NewPasswordG, 
        name="new_passwordg"),
    
    url(regex=r'^new_passworda/$',
        view=NewPasswordA, 
        name="new_passworda"),
    
    url(regex=r'^login_admin/$',
        view=LoginAdmin, 
        name="login_admin"),
    
    url(regex=r'^dashboard_admin/$',
        view=DashboardAdmin, 
        name="dashboard_admin"),
    
    url(regex=r'^aceptar_cuentas/$',
        view=AceptarCuentas, 
        name="aceptar_cuentas"),
    
    url(regex=r'^dashboard_egresado/$',
        view=DashboardEgresado, 
        name="dashboard_egresado"), 
    
    url(regex=r'^dashboard_root/$',
        view=DashboardRoot, 
        name="dashboard_root"),
    
    url(regex=r'^aceptar_cuentas_admin/$',
        view=AceptarCuentasAdmin, 
        name="aceptar_cuentas_admin"),

    url(regex=r'^crear_categorias/$',
        view=CreateCategory, 
        name="crear_categorias"),
    
    url(regex=r'^logout/$',
        view=closeSession, 
        name="logout"),
    
    url(regex=r'^reset/password_reset/$',
        view=PasswordReset,
        name="password_reset"
    ),
    
    url(regex=r'^reset/password_reset_done/$',
        view=PasswordResetDone,
        name='password_reset_done'
    ),
    
    url(regex=r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        view= PasswordResetConfirm,
        name='password_reset_confirm'
        ),
    
    url(regex=r'^reset/password_reset_complete/$',
        view= PasswordResetComplete,
        name = 'password_reset_complete'
    ),

    url(regex=r'^edit_info_adm/$',
        view= EditInfoAdm,
        name = 'edit_info_adm'
    ),

    url(regex=r'^register_done/$',
        view= RegisterDone,
        name = 'register_done'
    ),


    url(regex=r'^create_activity/$',
        view= CreateActivity,
        name = 'create_activity'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
