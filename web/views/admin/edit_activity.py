from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from domain.models import Admin , Activity

def EditActivity(request):
    mensaje = (False,'')
    dni = request.GET.get('dni')
    id_categoria = request.GET.get('id')
    usuario = []

    if request.method == 'GET':
        dni = request.GET.get('dni')
        id_categoria = request.GET.get('id')
        usuario = Admin.objects.filter(dni=dni)
        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('Admin/editarActividad.html')
        else:
            return redirect('/login_admin')

    if request.method == 'POST' :
        pass

    actividad = Activity.objects.get(id__exact=id_categoria)
    print (actividad)
    template = loader.get_template('Admin/editarActividad.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario,
        'actividad' : actividad,
    }
    return HttpResponse(template.render(ctx,request))