from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader


def DashboardEgresado(request):
    mensaje = (False,'')
    if request.user is None or not request.user.is_authenticated():
        return redirect('/login_egresado')
    template = loader.get_template('Egresado/dashboardEgresado.html')
    ctx = { 'mensaje': mensaje,
    }   
    return HttpResponse(template.render(ctx,request))