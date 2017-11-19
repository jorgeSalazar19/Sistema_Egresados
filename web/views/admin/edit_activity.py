from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from domain.models import Admin , Activity
import re

patron_nombre = re.compile('([A-ZÁÉÍÓÚa-zñáéíóú]{1}[a-zñáéíóúA-ZÁÉÍÓÚ]+)')
patron_descripcion = re.compile('([A-ZÁÉÍÓÚa-zñáéíóú]{1}[a-zñáéíóúA-ZÁÉÍÓÚ]+[\s]*)+')

def EditActivity(request):
    mensaje = (False,'')
    dni = request.GET.get('dni')
    id_categoria = request.GET.get('id')

    actividad = Activity.objects.get(id__exact=id_categoria)

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
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)
        usuario = usuario[0]

        name = request.POST.get('name')
        description = request.POST.get('description')

        mensajes_e = [] 
        if len(name) != 0 and re.match(patron_nombre, name) is not None:
            actividad.name = name
            actividad.save()

        else:
            error = "Tienes un error en el campo nombre de actividad"
            mensajes_e.append(error)
            mensaje = (True , mensajes_e)

        if len(description) != 0 and re.match(patron_descripcion,description) is not None:
            actividad.description = description
            actividad.save()

        else:
            error = "Tienes un error en el campo descripción de actividad"
            mensajes_e.append(error)
            mensaje = (True , mensajes_e)

        if len(request.FILES) != 0:
            image_activity =  request.FILES['image_activity']
        else:
            image_activity = None

        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)
        usuario = usuario[0]
        
        if image_activity is not None:
            actividad.image_activity.delete()
            actividad.image_activity = image_activity
            actividad.save()
            mensaje = (True ,'Imagen cargada correctamente')

    template = loader.get_template('Admin/editarActividad.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario,
        'actividad' : actividad,
    }
    return HttpResponse(template.render(ctx,request))