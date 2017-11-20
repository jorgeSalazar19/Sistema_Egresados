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
    
    url(regex=r'^dashboard_egresado/new_passwordg/$',
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

    url(regex=r'^lista_categorias/$',
        view=ListCategory, 
        name="lista_categorias"),

    url(regex=r'^delete_categorias/$',
        view=DeleteCategory, 
        name="delete_categorias"),
    
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

    url(regex=r'^list_activity/$',
        view= ListActivity,
        name = 'list_activity'
    ),

    url(regex=r'^create_activity/$',
        view= CreateActivity,
        name = 'create_activity'
    ),

    url(regex=r'^edit_activity/$',
        view= EditActivity,
        name = 'edit_activity'
    ),

    url(regex=r'^dashboard_egresado/preferences_graduated/$',
        view= PreferencesGraduated,
        name = 'preferences_graduated'
    ),

        url(regex=r'^dashboard_egresado/circulo_amigos/$',
        view= CirculoAmigos,
        name = 'circulo_amigos'
    ),

    url(regex=r'^dashboard_egresado/edit_info_gra/$',
        view= EditInfoGra,
        name = 'edit_info_gra'
    ),

    url(regex=r'^dashboard_egresado/send_email/$',
        view= SendEmail,
        name = 'send_email'
    ),

    url(regex=r'^dashboard_egresado/profile_graduated/$',
        view= ProfileGraduated,
        name = 'profile_graduated'
    ),

    url(regex=r'^success_category/$',
        view= SuccessCategory,
        name = 'success_category'
    ),

    url(regex=r'^success_activity/$',
        view= SuccessActivity,
        name = 'success_activity'
    ),

    url(regex=r'^success_edition/$',
        view= SuccessEdition,
        name = 'success_edition'
    ),

    url(regex=r'^success_profile_edition/$',
        view= SuccessProfileEdition,
        name = 'success_profile_edition'
    ),

    url(regex=r'^success_profile_edition_graduated/$',
        view= SuccessProfileEditionGraduated,
        name = 'success_profile_edition_graduated'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
