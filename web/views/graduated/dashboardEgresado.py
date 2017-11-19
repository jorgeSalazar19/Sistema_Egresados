from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate 
from domain.models import Category,Graduated,Activity
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta


def DashboardEgresado(request):

    dni = request.GET.get('username')
    dni_sugerencia = request.GET.get('dni')
    password = request.GET.get('password')
    mensaje = (False,'')
    template = loader.get_template('Egresado/dashboardEgresado.html')
    usuario = Graduated.objects.get(dni=dni) 
    categorias = usuario.preferences.all()
    categorias_A = []*len(categorias)
    usuario_agregar = None

    if dni_sugerencia is not None:
        usuario_agregar = Graduated.objects.get(dni__exact=dni_sugerencia)

    if usuario_agregar is not None:
        usuario.friends.add(usuario_agregar)

    for category in categorias:
        categorias_A.append(category)
    actividades = Activity.objects.all()

    actividades_egresado = []
    for activity in actividades:
        for category in categorias_A:
            if str(activity.category.name) == str(category):
                actividades_egresado.append(activity)

    usuario_f = Graduated.objects.get(dni=dni)
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

    usuario = Graduated.objects.filter(dni=dni)
    ctx = { 'mensaje': mensaje,
            'actividades':actividades_egresado,
            'usuario' : usuario[0],
            'amigos' : friends,
            'sugerencias' : sugerencias_s,
        } 

    if len(usuario) == 0 or not request.user.is_authenticated():
        return redirect('/login_egresado')

    else:
        if usuario[0].first_login == 0:
            return redirect('/dashboard_egresado/new_passwordg?dni='+dni)

        else:
            return HttpResponse(template.render(ctx,request))

    return HttpResponse(template.render(ctx,request))
