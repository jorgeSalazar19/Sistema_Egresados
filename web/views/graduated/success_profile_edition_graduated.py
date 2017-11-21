from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from domain.models import Graduated 

def SuccessProfileEditionGraduated(request):
    mensaje = (False,'')
    usuario = []

    if request.method == 'GET':
        username = request.GET.get('username')
        usuario = Graduated.objects.filter(dni=username)

        if str(request.user) == str(username) and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('Egresado/perfilEditado.html')
        else:
            return redirect('/login_egresado')

    template = loader.get_template('Egresado/perfilEditado.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario,
    }
    return HttpResponse(template.render(ctx,request))