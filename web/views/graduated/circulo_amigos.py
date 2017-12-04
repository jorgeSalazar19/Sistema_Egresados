from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Graduated
from dateutil.relativedelta import relativedelta

def CirculoAmigos(request):
    username = request.GET.get('username')

    if str(request.user) != str(username) or not request.user.is_authenticated():
        return redirect('/login_egresado')

    mensaje = (False , "")
    usuario_agregar = None
    usuario = Graduated.objects.filter(dni=username)
    dni_sugerencia = request.GET.get('dni')
    usuario_f = Graduated.objects.get(dni=username)

    if dni_sugerencia is not None:
        usuario_agregar = Graduated.objects.get(dni__exact=dni_sugerencia)

    if usuario_agregar is not None:
        usuario_f.friends.add(usuario_agregar)
        mensaje = (True, "Se ha agregado correctamente al usuario "+ usuario_agregar.user.first_name+ " " + usuario_agregar.user.last_name )

    
    graduation_year_user = usuario_f.graduation_year
    limite_inferior = graduation_year_user - relativedelta(years=10)
    limite_superior = graduation_year_user + relativedelta(years=10)
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