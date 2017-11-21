from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from domain.models import Admin 
def SuccessActivity(request):
    mensaje = (False,'')
    usuario = []

    if request.method == 'GET':
        dni = request.GET.get('dni')
        
        if str(request.user) == str(dni) and request.user.is_authenticated():
            usuario = Admin.objects.filter(dni=dni)
            usuario = usuario[0]
            template = loader.get_template('Admin/actividadCreada.html')
        else:
            return redirect('/login_admin')

    template = loader.get_template('Admin/actividadCreada.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario,
    }
    return HttpResponse(template.render(ctx,request))