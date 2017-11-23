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
        print(username)
        usuario = User.objects.filter(username=username)
        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
        else:
            return redirect('/')

    if request.method == 'POST':
        
        accion = request.POST.get('accion')
        id_admin , accion , username = accion.split(' ')
        usuario = User.objects.get(username=username)
        
        if accion == 'Deshabilitar':
            admin = Admin.objects.filter(dni__exact=id_admin)
            admin = admin[0]
            admin.is_active = False
            admin.save()
            mensaje = (True , "Usuario "+ admin.user.first_name +" " + admin.user.last_name +" deshabilitado")

        if accion == 'Habilitar':
            admin = Admin.objects.filter(dni__exact=id_admin)
            admin = admin[0]
            admin.is_active =True
            admin.save()
            mensaje = (True , "Usuario "+ admin.user.first_name +" " + admin.user.last_name +" habilitado")

        if accion == 'Eliminar':
            admin = Admin.objects.filter(dni__exact=id_admin)
            admin = admin[0]
            mensaje = (True , "Usuario "+ admin.user.first_name +" " + admin.user.last_name +" eliminado")
            egresado = Graduated.objects.filter(dni__exact=id_admin)
            if len(egresado) == 0:
                admin.user.delete()
                admin.delete()
            else:
                admin.user.is_staff = False
                admin.user.save()
                admin.delete()



    administradores = Admin.objects.all()
    template = loader.get_template('Root/GestionCuentas.html')
    ctx = {
            'mensaje' : mensaje,
            'usuario' : usuario,
            'admins' : administradores,
    }
    return HttpResponse(template.render(ctx,request))