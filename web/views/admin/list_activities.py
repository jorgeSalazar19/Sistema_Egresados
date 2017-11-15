from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from domain.models import Admin , Activity

def ListActivity(request):
    mensaje = (False,'')
    usuario = []

    if request.method == 'GET':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)
        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('Admin/listaActividades.html')
        else:
            return redirect('/login_admin')

    if request.method == 'POST':
        Action_button = request.POST.get('tipo')
        id_activity , action = Action_button.split()

        if action == "Eliminar":
            actividad = Activity.objects.filter(id__exact=id_activity)
            actividad.delete()

    actividades = Activity.objects.all().order_by('name')
    template = loader.get_template('Admin/listaActividades.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario,
        'actividades' : actividades,
    }
    return HttpResponse(template.render(ctx,request))