from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login , authenticate 
from django.contrib.auth.models import User
from domain.models import Graduated , Category

def LoginEgresado(request):
    error = (False, "")
    dato_username = []
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = Graduated.objects.filter(dni=username)
        dato_username = request.POST
        if len(usuario) != 0:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard_egresado?dni="+username)
            else:
                error = (True, "Contraseña no valida")
        else:
            usuario = User.objects.filter(username=username)
            if len(usuario) != 0:
                user = authenticate(username=username, password=password)
                usuario = usuario[0]
                if user is not None and usuario.is_superuser:
                    login(request,user)
                    return redirect("/dashboard_root?username="+username)

                else:
                    error = (True , "Contraseña no valida " )

            else:
                error = (True, "No existe el usuario " + username)

    template = loader.get_template('login.html')
    ctx = { 'error': error,
            'dato' : dato_username,
    }   
    return HttpResponse(template.render(ctx,request))


