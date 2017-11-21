from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Graduated
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail

def SendEmail(request):

    if request.method == 'GET':
        username = request.GET.get('username')
        dni = request.GET.get('dni')
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
        mensaje = request.POST.get('mensaje')
        print(usuario.user.email)

        mensaje = 'el usuario ' + usuario.user.first_name + " " + usuario.user.last_name + ' ' + 'te ha enviado un mensaje' + "\n" + mensaje
        email = EmailMessage(asunto, mensaje, 'jorgemsm12316@gmail.com' , [amigo.email])
        email.send(fail_silently=True)

        return redirect('/success_send_mail?username='+username)

    template = loader.get_template('Egresado/enviarCorreo.html')
    ctx = {
         'usuario' : usuario,
    }

    return HttpResponse(template.render(ctx,request))