from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login , authenticate
from django.contrib.auth.models import User
from domain.models import Graduated

def LoginEgresado(request):
    error = (False, "")
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        
        usuario = User.objects.filter(username=username)
        if len(usuario) != 0:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard_egresado")
            else:
                error = (True, "Password no valida")
        else:
            error = (True, "No existe el usuario " + username)
#    Graduateds = Graduated.objects.all()
#    for graduated in Graduateds:
#        print(graduated.user.email)
    template = loader.get_template('login.html')
    ctx = { 'error': error,
    }   
    return HttpResponse(template.render(ctx,request))