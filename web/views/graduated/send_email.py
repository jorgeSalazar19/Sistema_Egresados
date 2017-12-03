from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Graduated , Historial
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from datetime import date
from django.conf import settings

def SendEmail(request):

    if request.method == 'GET':
        username = request.GET.get('username')
        dni = request.GET.get('dni')

        if str(request.user) != str(username) or not request.user.is_authenticated():
            return redirect('/login_egresado')


        usuario = Graduated.objects.filter(dni=username)
        usuario = usuario[0]
        amigo = User.objects.filter(username=dni)
        amigo = amigo[0]
        print(amigo.email)

    if request.method == 'POST':
        username = request.GET.get('username')
        usuario = Graduated.objects.filter(dni=username)
        usuario = usuario[0]

        dni = request.GET.get('dni')
        amigo = User.objects.filter(username=dni)
        amigo = amigo[0]

        asunto = request.POST.get('asunto')
        mensaje_r = request.POST.get('mensaje')
        from_email = settings.EMAIL_HOST_USER

        mensaje = 'el usuario ' + usuario.user.first_name + " " + usuario.user.last_name + ' ' + 'te ha enviado el siguiente mensaje:' + "\n" + mensaje_r
        email = EmailMessage(asunto, mensaje, from_email , [amigo.email])
        email.send(fail_silently=True)

        email_send = Historial.objects.create(
                            from_email=usuario.user.email,
                            to_email=amigo.email,
                            subject=asunto,
                            message=mensaje_r,
                            date_email=date.today()

                                            )
        email_send.save()

        return redirect('/success_send_mail?username='+username)

    template = loader.get_template('Egresado/enviarCorreo.html')
    ctx = {
         'usuario' : usuario,
    }

    return HttpResponse(template.render(ctx,request))