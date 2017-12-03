from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from domain.models import PreRegisterAdmin , Admin

from ...services import UserService
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User

def AceptarCuentasAdmin(request):
    mensaje = (False , "")
    usuario = []
    if request.method == 'GET':
        username = request.GET.get('username')
        id_p = request.GET.get('id')
        accion = request.GET.get('action')
        print(username,id_p,accion)
        usuario = User.objects.filter(username=username)

        if id_p != None:
            preregister = PreRegisterAdmin.objects.get(id__exact=id_p)

            if accion == 'Aceptar':
                mensaje = (True , "Usuario Creado con exito")
                try:
                    user_data = preregister.__dict__
                    user_data['temporal_password'] = get_random_string(length=12)
                    user_service = UserService(user_data)
                    user_service.register_admin()
                    from_email = settings.EMAIL_HOST_USER
                    to_list = [user_data['email'],settings.EMAIL_HOST_USER]
                    current_site = get_current_site(request)
                    SendMail(from_email,to_list,user_data['temporal_password'],current_site)
                except Exception as e:
                    print (e)
                    mensaje = (True , str(e))

            if accion == 'Eliminar':
                mensaje = (True , "Usuario eliminado con exito")
                preregister.delete()


        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
        else:
            return redirect('/login_admin')

    template = loader.get_template('Root/aceptarCuentasAdmin.html')
    pre_registros = PreRegisterAdmin.objects.all()
    ctx = {
    'mensaje': mensaje,
    'pre_registros' : pre_registros,
    'usuario' : usuario,
    }   
    return HttpResponse(template.render(ctx,request))

def SendMail(fromEmail,to_list,t_password,current_site):
    subject, from_email, to = 'Sistema Egresados -- Contraseña', fromEmail, to_list
    message = render_to_string('FormatosCorreo/FormatoPasswordAdmin.html', {
        'domain' : current_site.domain,
        'password' : t_password
        })
    email = EmailMessage(subject, message, from_email, to)
    email.send()
