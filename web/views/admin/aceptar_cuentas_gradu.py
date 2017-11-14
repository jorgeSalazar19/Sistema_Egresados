from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from domain.models import PreRegisterGraduated , Graduated , Admin

from ...services import UserService
from django.core.mail import EmailMessage
from django.conf import settings

def AceptarCuentas(request):
    mensaje = (False,'')
    usuario = []
    if request.method == 'GET':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)

        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('Admin/aceptarCuentas.html')
            pre_registros = PreRegisterGraduated.objects.all()
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
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)
        usuario = usuario[0]
        preregister = PreRegisterGraduated.objects.get(id=id_pregister)
        if action == "Aceptar":
            user_data = preregister.__dict__
            user_data['temporal_password'] = get_random_string(length=12)
            try:
                user_service = UserService(user_data)
                user_service.register_graduated()
                from_email = settings.EMAIL_HOST_USER
                to_list = [user_data['email'],settings.EMAIL_HOST_USER]
                current_site = get_current_site(request)
                SendMail(from_email,to_list,user_data['temporal_password'],current_site)
            except Exception as e:
                mensaje = (True , str(e))
            
        if action == "Eliminar":
            preregister.delete()

    template = loader.get_template('Admin/aceptarCuentas.html')
    pre_registros = PreRegisterGraduated.objects.all()
    ctx = { 'mensaje': mensaje,
            'pre_registros': pre_registros,
            'usuario' : usuario,
    }   
    return HttpResponse(template.render(ctx,request))

    
def SendMail(fromEmail,to_list,t_password,current_site):
    subject, from_email, to = 'Sistema Egresados -- Contraseña', fromEmail, to_list
    message = render_to_string('FormatosCorreo/FormatoPassword.html', {
        'domain' : current_site.domain,
        'password' : t_password
        })
    email = EmailMessage(subject, message, from_email, to)
    email.send()
