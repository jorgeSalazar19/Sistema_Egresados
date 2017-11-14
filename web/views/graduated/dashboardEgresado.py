from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate 
from domain.models import Category,Graduated,Activity
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash


def DashboardEgresado(request):
    dni = request.GET.get('username')
    password = request.GET.get('password')
    mensaje = (False,'')
    template = loader.get_template('Egresado/dashboardEgresado.html')
    usuario = Graduated.objects.get(dni=dni) 
    categorias = usuario.preferences.all()
    categorias_A = []*len(categorias)
    for category in categorias:
        categorias_A.append(category)
    actividades = Activity.objects.all()

    actividades_egresado = []
    for activity in actividades:
        for category in categorias_A:
            if str(activity.category.name) == str(category):
                actividades_egresado.append(activity)

    ctx = { 'mensaje': mensaje,
            'actividades':actividades_egresado,
            'usuario' : usuario,
            } 
    usuario = Graduated.objects.filter(dni=dni)
    print(request.user.is_authenticated())
    if len(usuario) == 0 or not request.user.is_authenticated():
        return redirect('/login_egresado')
    else:
        if usuario[0].first_login == 0:
            return redirect('/dashboard_egresado/new_passwordg?dni='+dni)
        else:
            return HttpResponse(template.render(ctx,request))

    return HttpResponse(template.render(ctx,request))
