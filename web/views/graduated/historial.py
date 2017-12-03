from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Graduated , Historial
from django.contrib.auth.models import User

def HistorialEmails(request):
    usuario = 0
    historial = 0

    if request.method == 'GET':

        username = request.GET.get('username')
        dni = request.GET.get('dni')

        print(username)
        usuario = Graduated.objects.filter(dni__exact=username)
        usuario = usuario[0]
        print(usuario)

        print(usuario.user.email)
        historial = Historial.objects.filter(from_email__exact=usuario.user.email)
        print(historial)

        if str(request.user) != str(username) or not request.user.is_authenticated():
            return redirect('/login_egresado')

    print(usuario)
    template = loader.get_template('Egresado/historial.html')
    ctx = {
         'usuario' : usuario,
         'historial' : historial,
    }

    return HttpResponse(template.render(ctx,request))

