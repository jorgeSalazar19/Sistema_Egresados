from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from domain.models import PreRegisterGraduated , Graduated , Admin

from ..services import UserService
from django.core.mail import EmailMessage
from django.conf import settings

def DashboardAdmin(request):
    mensaje = (False,'')
    if request.method == 'GET':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)

        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('DashBoardAdmin.html')
            pre_registros = PreRegisterGraduated.objects.all()
            ctx = { 'mensaje': mensaje,
            'pre_registros': pre_registros,
            'usuario' : usuario,
            }   
            return HttpResponse(template.render(ctx,request))
        else:
            return redirect('/login_admin')
    

def AceptarCuentas(request):
    mensaje = (False,'')
    if request.method == 'GET':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)

        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('aceptarCuentas.html')
            pre_registros = PreRegisterGraduated.objects.all()
            print("aca: " , usuario)
            ctx = { 'mensaje': mensaje,
                    'pre_registros': pre_registros,
                    'usuario' : usuario,
            }   
            return HttpResponse(template.render(ctx,request))
        else:
            return redirect('/login_admin')

    if request.method == 'POST':
        Action_button = request.POST.get('tipo')
        id_pregister , action = Action_button.split()
        preregister = PreRegisterGraduated.objects.get(id=id_pregister)
        if action == "Aceptar":
            user_data = preregister.__dict__
            user_data['temporal_password'] = get_random_string(length=12)
            try:
                user_service = UserService(user_data)
                user_service.register_graduated()
                from_email = settings.EMAIL_HOST_USER
                to_list = [user_data['email'],settings.EMAIL_HOST_USER]
                SendMail(from_email,to_list,user_data['temporal_password'])
            except Exception as e:
                mensaje = (True , str(e))
            
        if action == "Eliminar":
            preregister.delete()

    template = loader.get_template('aceptarCuentas.html')
    pre_registros = PreRegisterGraduated.objects.all()
    ctx = { 'mensaje': mensaje,
            'pre_registros': pre_registros,
    }   
    return HttpResponse(template.render(ctx,request))

    
def SendMail(fromEmail,to_list,t_password):
    subject, from_email, to = 'Sistema Egresados -- Contraseña', fromEmail, to_list
    title = "<h1>Bienvenido al sistema de Egresados</h1><br>"
    body = "<p><h3>Tu cuenta de egresado UTP ha sido activada y tu contraseña es: </h3></p>" + t_password + "----->"
    link = "<a href='http://127.0.0.1:8000/login_egresado/'>Presiona Aca para iniciar Sesión</a>"
    html_content = title + body + link
    email = EmailMessage(subject, html_content, from_email, to)
    email.content_subtype = "html"
    email.send()