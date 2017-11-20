from .admin.dashboardAdmin import DashboardAdmin
from .admin.aceptar_cuentas_gradu import AceptarCuentas
from .admin.login_admin import LoginAdmin , NewPasswordA
from .admin.p_register_admin import PreRegisterAdmin
from .admin.edit_info_adm import EditInfoAdm
from .admin.create_activity import CreateActivity
from .admin.list_activities import ListActivity
from .admin.edit_activity import EditActivity
from .admin.success_activity import SuccessActivity

from .graduated.dashboardEgresado import DashboardEgresado 
from .graduated.new_password import NewPasswordG
from .graduated.preferences_graduated import PreferencesGraduated
from .graduated.login_egresado import LoginEgresado 
from .graduated.p_register_graduated import PreRegisterGraduated
from .graduated.register_done import RegisterDone
from .graduated.circulo_amigos import CirculoAmigos

from .graduated.edit_inf_gra import EditInfoGra
from .graduated.send_email import SendEmail
from .graduated.profile_graduated import ProfileGraduated


from .superuser.dashboardRoot import DashboardRoot
from .superuser.aceptar_cuentas_admin import AceptarCuentasAdmin
from .superuser.create_category import CreateCategory
from .superuser.lista_categories import ListCategory
from .superuser.delete_categories import DeleteCategory
from .superuser.success_category import SuccessCategory


from .index import Index
from .logout import closeSession

from .password_reset import ( PasswordReset,
							  PasswordResetDone,
							  PasswordResetConfirm ,
							  PasswordResetComplete
							)							
