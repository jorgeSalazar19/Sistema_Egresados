from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Graduated
from django.contrib.auth.models import User
from django.contrib.auth import login ,  authenticate

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
            user = authenticate(request=request, username=dni, password=password)
            login(request , user)
            print(request.user.is_authenticated())
            return redirect("/dashboard_egresado/preferences_graduated?dni="+dni)
        else:
            error = "Las contraseñas no coinciden"


    template = loader.get_template('ChangePassword.html')
    ctx = { 'error': error,
    }   
    return HttpResponse(template.render(ctx,request))