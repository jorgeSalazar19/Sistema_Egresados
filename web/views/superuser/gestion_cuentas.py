from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User
from domain.models import Admin , Graduated

def AccountManagement(request):
    mensaje = (False,'')
    usuario = []
    if request.method == 'GET':

        username = request.GET.get('username')
        dni = request.GET.get('dni')
        accion = request.GET.get('action')

        print(username,dni,accion)

        if dni != None:
            admin = Admin.objects.filter(dni__exact=dni)
            admin = admin[0]
            egresado = Graduated.objects.filter(dni__exact=dni)
            if accion == 'Eliminar':
                mensaje = (True , "Usuario "+ admin.user.first_name +" " + admin.user.last_name +" eliminado")
                if len(egresado) == 0:
                    admin.user.delete()
                    admin.delete()
                    
                else:
                    admin.user.is_staff = False
                    admin.user.save()
                    admin.delete()
                    

            if accion == 'Deshabilitar':
                admin = Admin.objects.filter(dni__exact=dni)
                admin = admin[0]
                mensaje = (True , "Usuario "+ admin.user.first_name +" " + admin.user.last_name +" deshabiltado")
                admin.is_active = False
                admin.save()
                

            if accion == 'Habilitar':
                admin = Admin.objects.filter(dni__exact=dni)
                admin = admin[0]
                mensaje = (True , "Usuario "+ admin.user.first_name +" " + admin.user.last_name +" Habiltado")
                admin.is_active = True
                admin.save()


        
        usuario = User.objects.filter(username=username)
        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
        else:
            return redirect('/')


    administradores = Admin.objects.all()
    template = loader.get_template('Root/GestionCuentas.html')
    ctx = {
            'mensaje' : mensaje,
            'usuario' : usuario,
            'admins' : administradores,
    }
    return HttpResponse(template.render(ctx,request))