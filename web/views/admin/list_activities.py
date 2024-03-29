from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from domain.models import Admin , Activity

def ListActivity(request):
    mensaje = (False,'')
    usuario = []

    if request.method == 'GET':
        dni = request.GET.get('dni')
        id_a = request.GET.get('id')
        accion = request.GET.get('action')
        
        print(dni,id_a,accion)

        if id_a != None:
            actividad = Activity.objects.filter(id__exact=id_a)
            actividad = actividad[0]

            if accion == 'Eliminar':
                actividad.image_activity.delete()
                mensaje = (True , "la actividad "+"'"+actividad.name+"'"+ " fue eliminada con exito" )
                actividad.delete()


        if str(request.user) == str(dni) and request.user.is_authenticated():
            usuario = Admin.objects.filter(dni=dni)
            usuario = usuario[0]
            template = loader.get_template('Admin/listaActividades.html')
        else:
            return redirect('/login_admin')

    actividades = Activity.objects.all().order_by('name')
    template = loader.get_template('Admin/listaActividades.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario,
        'actividades' : actividades,
    }
    print(mensaje)
    return HttpResponse(template.render(ctx,request))