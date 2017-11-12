from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes , force_text
from domain.models import PreRegisterGraduated , Graduated , Admin
from ..token import account_activation_token

from ..services import UserService
from django.core.mail import EmailMessage
from django.conf import settings

def PasswordReset(request):
    mensaje = (False,'')
    email = " "
    if request.method == 'POST':
        email = request.POST.get('correo')
        email_user = User.objects.filter(email=email)
        if len(email_user) != 0:
            user = email_user[0]
            from_email = settings.EMAIL_HOST_USER
            to_list = [email,settings.EMAIL_HOST_USER]
            current_site = get_current_site(request)
            SendMail(from_email,to_list,current_site,user,email_user)
            return redirect("/reset/password_reset_done")
        else:
            mensaje = (True,'El correo no esta en nuestra base de datos')

    tempĺate = loader.get_template('ResetPassword/IngresoCorreo.html')
    ctx = { 'mensaje': mensaje,
            'email': email,
    }   
    return HttpResponse(tempĺate.render(ctx,request))

def PasswordResetDone(request):
    template = loader.get_template('ResetPassword/InformacionCorreo.html')
    ctx = {}
    return HttpResponse(template.render(ctx,request))

def PasswordResetConfirm(request, uidb64 , token):
    template = loader.get_template('ResetPassword/ConfirmarContraseña.html')
    ctx = {}
    if request.method == 'GET':
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            print(account_activation_token.check_token(user, token))
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            return HttpResponse(template.render(ctx,request))
        else:
            template = loader.get_template('ResetPassword/MensajeLinkInvalido.html')
            ctx = {}
            return HttpResponse(template.render(ctx,request))

    elif request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            uid = force_text(urlsafe_base64_decode(uidb64))
            usuario = User.objects.get(pk=uid)
            usuario.set_password(password1)
            usuario.save()
            return redirect('/reset/password_reset_complete/')
        else:
            mensaje = (True , 'Las contraseñas No coinciden')
            ctx = {
                    'mensaje' : mensaje,
            }
            return HttpResponse(template.render(ctx,request))


def PasswordResetComplete(request):
    template = loader.get_template('ResetPassword/ConfirmacionCambioC.html')
    ctx = {}
    return HttpResponse(template.render(ctx,request))

def SendMail(from_email,to_list,current_site,user,UserT):
    subject, from_email, to = 'Sistema Egresados -- Recuperación Contraseña',from_email, to_list
    message = render_to_string('ResetPassword/FormatoCorreo.html' , {
            'user' : user,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
            'token' : account_activation_token.make_token(user),
        })
    email = EmailMessage(subject, message , from_email, to)
    email.send()

