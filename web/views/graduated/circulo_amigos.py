from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Graduated
from dateutil.relativedelta import relativedelta

def CirculoAmigos(request):

    mensaje = (True , "")
    username = request.GET.get('username')
    usuario = Graduated.objects.filter(dni=username)
    usuario_f = Graduated.objects.get(dni=username)

    
    graduation_year_user = usuario_f.graduation_year
    limite_inferior = graduation_year_user - relativedelta(years=2)
    limite_superior = graduation_year_user + relativedelta(years=2)
    career_user = usuario_f.career
    dni_user = usuario_f.dni

    friends = usuario_f.friends.all().exclude(dni__exact=dni_user)
    sugerencias = Graduated.objects.filter(graduation_year__lt=( limite_superior) ,
                                      graduation_year__gt=(limite_inferior),career__exact=career_user).exclude(dni__exact=dni_user)

    sugerencias_s = []
    for sugerencia in sugerencias:
        if sugerencia in friends:
            print("esta")
        else:
            sugerencias_s.append(sugerencia)
            
    template = loader.get_template('Egresado/circuloAmigos.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario[0],
        'amigos' : friends,
        'sugerencias' : sugerencias_s,
    }
    return HttpResponse(template.render(ctx,request))