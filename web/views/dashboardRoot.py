from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from domain.models import PreRegisterAdmin , Admin

from ..services import UserService
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User


def DashboardRoot(request):
    mensaje = (False,'')

    if request.method == 'GET':
        username = request.GET.get('username')
        usuario = User.objects.filter(username=username)

        if len(usuario) != 0:
            usuario = usuario[0]
            template = loader.get_template('DashBoardRoot.html')
            ctx = { 'mensaje': mensaje,
            'usuario' : usuario,
            }   
            return HttpResponse(template.render(ctx,request))

            
    if request.user is None or not request.user.is_authenticated():
        return redirect('/')



def AceptarCuentasAdmin(request):
    mensaje = (False , "")

    if request.method == 'GET':
        username = request.GET.get('username')
        usuario = User.objects.filter(username=username)
        if len(usuario) != 0:
            usuario = usuario[0]
            print('usuario' , usuario)
            template = loader.get_template('aceptarCuentasAdmin.html')
            pre_registros = PreRegisterAdmin.objects.all()
            ctx = { 'mensaje': mensaje,
                    'pre_registros' : pre_registros,
                    'usuario' : usuario,
            }   
            return HttpResponse(template.render(ctx,request))

    if request.method == 'POST':
        Action_button = request.POST.get('tipo')
        id_pregister , action = Action_button.split()
        preregister = PreRegisterAdmin.objects.get(id=id_pregister)
        if action == "Aceptar":

            try:
                user_data = preregister.__dict__
                user_data['temporal_password'] = get_random_string(length=12)
                user_service = UserService(user_data)
                user_service.register_admin()
                from_email = settings.EMAIL_HOST_USER
                to_list = [user_data['email'],settings.EMAIL_HOST_USER]
                SendMail(from_email,to_list,user_data['temporal_password'])
            except Exception as e:
                mensaje = (True , str(e))

        if action == "Eliminar":
            preregister.delete()

    template = loader.get_template('aceptarCuentasAdmin.html')
    pre_registros = PreRegisterAdmin.objects.all()
    ctx = { 'mensaje': mensaje,
    'pre_registros' : pre_registros,
    }   
    return HttpResponse(template.render(ctx,request))

def SendMail(fromEmail,to_list,t_password):
    subject, from_email, to = 'Sistema Egresados -- Contraseña', fromEmail, to_list
    title = "<h1>Bienvenido al sistema de Egresados</h1><br>"
    body = "<p><h3>Tu cuenta de Administrador ha sido activada y tu contraseña es: </h3></p>" + t_password + "----->"
    link = "<a href='http://127.0.0.1:8000/login_egresado/'>Presiona Aca para iniciar Sesión</a>"
    html_content = title + body + link
    email = EmailMessage(subject, html_content, from_email, to)
    email.content_subtype = "html"
    email.send()