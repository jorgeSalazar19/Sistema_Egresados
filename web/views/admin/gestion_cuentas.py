from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User
from domain.models import Graduated , Admin

def AccountManagementE(request):
    mensaje = (False,'')
    usuario = []

    if request.method == 'GET':
        dni = request.GET.get('dni')
        accion = request.GET.get('action')
        dni_e = request.GET.get('dni_e')
        print(dni,accion,dni_e)
        usuario = Admin.objects.filter(dni=dni)

        if dni_e != None:
            if accion == 'Eliminar':
                egresado = Graduated.objects.filter(dni__exact=dni_e)
                egresado = egresado[0]
                mensaje = (True , "Usuario "+ egresado.user.first_name +" " + egresado.user.last_name +" eliminado")
                if egresado.user.is_staff:
                    egresado.delete()
                else:
                    egresado.user.delete()
                    egresado.delete()
            if accion == 'Deshabilitar':
                egresado = Graduated.objects.filter(dni__exact=dni_e)
                egresado = egresado[0]
                egresado.is_active = False
                egresado.save()
                mensaje = (True , "Usuario "+ egresado.user.first_name +" " + egresado.user.last_name +" deshabilitado")

            if accion == 'Habilitar':
                egresado = Graduated.objects.filter(dni__exact=dni_e)
                egresado = egresado[0]
                egresado.is_active =True
                egresado.save()
                mensaje = (True , "Usuario "+ egresado.user.first_name +" " + egresado.user.last_name +" habilitado")


        if len(usuario) != 0 and request.user.is_authenticated():
                usuario = usuario[0]
        else:
            return redirect('/')


    egresados = Graduated.objects.all().order_by('dni')
    template = loader.get_template('Admin/GestionCuentasE.html')
    ctx = {
            'mensaje' : mensaje,
            'usuario' : usuario,
            'egresados' : egresados,
    }
    return HttpResponse(template.render(ctx,request))