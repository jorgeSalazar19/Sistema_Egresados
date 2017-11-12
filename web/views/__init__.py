from .admin.dashboardAdmin import DashboardAdmin
from .admin.aceptar_cuentas_gradu import AceptarCuentas
from .admin.login_admin import LoginAdmin , NewPasswordA
from .admin.p_register_admin import PreRegisterAdmin
from .admin.edit_info_adm import EditInfoAdm
from .admin.create_activity import CreateActivity

from .graduated.dashboardEgresado import DashboardEgresado , NewPasswordG , PreferencesGraduated
from .graduated.login_egresado import LoginEgresado 
from .graduated.p_register_graduated import PreRegisterGraduated
from .graduated.register_done import RegisterDone

from .superuser.dashboardRoot import DashboardRoot
from .superuser.aceptar_cuentas_admin import AceptarCuentasAdmin
from .superuser.create_category import CreateCategory

from .index import Index
from .logout import closeSession

from .password_reset import ( PasswordReset,
							  PasswordResetDone,
							  PasswordResetConfirm ,
							  PasswordResetComplete
							)							
