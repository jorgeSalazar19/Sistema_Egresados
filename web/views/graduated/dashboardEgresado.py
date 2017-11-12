from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate 
from domain.models import Category,Graduated,Activity
from django.contrib.auth.models import User


def DashboardEgresado(request):
    dni = request.GET.get('dni')
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
            } 
    usuario = Graduated.objects.filter(dni=dni)
    if len(usuario) == 0 or not request.user.is_authenticated():
        print(dni)
        print(password)
        print('entra')
        return redirect('/login_egresado')
    else:
        if usuario[0].first_login == 0:
            print('entra')
            return redirect('/dashboard_egresado/new_passwordg?dni='+dni)
        else:
            return HttpResponse(template.render(ctx,request))

    return HttpResponse(template.render(ctx,request))

def NewPasswordG(request):
    error = ""
    dni = request.GET.get('dni')
    password = request.GET.get('password')
    usuario = Graduated.objects.get(dni=dni)

    if request.method == "POST":
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            usuario.first_login = 1
            usuario.save()
            usuario.user.set_password(password)
            usuario.user.save()
            return redirect("/dashboard_egresado/preferences_graduated?dni="+dni)
        else:
            error = "Las contraseñas no coinciden"


    template = loader.get_template('ChangePassword.html')
    ctx = { 'error': error,
    }   
    return HttpResponse(template.render(ctx,request))

def PreferencesGraduated(request):
    mensaje = (False,'')
    dni = request.GET.get('dni')
    password = request.GET.get('password')
    usuario = Graduated.objects.get(dni=dni)
    print(password)
    if request.method == 'POST':
        ids_categoria = request.POST.getlist('categorias')    
        categorias = []*len(ids_categoria)
        for i in range(len(ids_categoria)):
            id=ids_categoria[i]
            categoria = Category.objects.get(id=id)
            categorias.append(categoria)

        if len(categorias) != 0:
            usuario.preferences = categorias
            usuario.save()
            return redirect('/dashboard_egresado?username='+dni)

        else :
            mensaje = (True , "Por favor seleccione por lo menos una categoria como preferencia")
            


    template = loader.get_template('Egresado/preferencias.html')
    categorias = Category.objects.all().order_by('name')
    ctx = { 'mensaje': mensaje,
            'categorias' : categorias,
    }   
    return HttpResponse(template.render(ctx,request))