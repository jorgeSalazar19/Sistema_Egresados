from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from domain.models import Admin , Activity

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

        if len(name) != 0:
            actividad.name = name
            actividad.save()

        if len(description) != 0:
            actividad.description = description
            actividad.save()

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
        else:
            mensaje = (True, 'No se cargo')

    
    print (actividad)
    template = loader.get_template('Admin/editarActividad.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario,
        'actividad' : actividad,
    }
    return HttpResponse(template.render(ctx,request))