from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from domain.models import Admin


def LoginAdmin(request):
    error = (False, "")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = Admin.objects.filter(dni=username)
        if len(usuario) != 0:
            user = authenticate(username=username, password=password)
            if user is not None:
                usuario = usuario[0]
                login(request, user)
                if usuario.first_login == 0:
                    usuario.first_login = 1
                    usuario.save()
                    return redirect("/new_passworda?dni="+username)
                else:
                    return redirect("/dashboard_admin")
            else:
                error = (True, "Password no valida")
        else:
            usuario = User.objects.filter(username=username)
            if len(usuario) != 0:
                user = authenticate(username=username, password=password)
                usuario = usuario[0]
                if user is not None and usuario.is_superuser:
                    login(request,user)
                    return redirect("/dashboard_root")

                else:
                    error=(True , "Password no valida")

            else:
                error = (True, "No existe el usuario " + username)

    template = loader.get_template('login.html')
    ctx = {
        'error': error, 
    }
    return HttpResponse(template.render(ctx, request))

def NewPasswordA(request):
    error = ""
    dni = request.GET.get('dni')
    usuario = Admin.objects.get(dni=dni)

    if request.method == "POST":
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            usuario.user.set_password(password)
            usuario.user.save()
            return redirect("/dashboard_admin")
        else:
            error = "Las contraseñas no coinciden"


    template = loader.get_template('ChangePassword.html')
    ctx = { 'error': error,
    }   
    return HttpResponse(template.render(ctx,request))