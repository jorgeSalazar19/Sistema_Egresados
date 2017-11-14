from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Graduated

def CirculoAmigos(request):
    mensaje = (False,'')
    username = request.GET.get('username')
    print(username)
    usuario = Graduated.objects.filter(dni=username)
    template = loader.get_template('Egresado/circuloAmigos.html')
    usuario = usuario[0]
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario
    }
    return HttpResponse(template.render(ctx,request))