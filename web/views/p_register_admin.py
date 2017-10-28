from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from web.forms import RegisterFormAdmin


from domain.models import Country , PreRegisterAdmin as PreRegister, Admin
from django.contrib.auth.models import User


def PreRegisterAdmin(request):
    mensaje = (False,'')
    if request.method == 'POST':
        id_pregister = request.POST.get('dni')
        email_pregister = request.POST.get('email')

        usuario_dni = PreRegister.objects.filter(dni=id_pregister)
        usuario_email = PreRegister.objects.filter(email=email_pregister)
        usuario_admin = Admin.objects.filter(dni=id_pregister)

        perfil_form = RegisterFormAdmin(data=request.POST)

        if perfil_form.is_valid():
            if (len(usuario_dni) == 0) and (len(usuario_email) == 0):
                if len(usuario_admin) == 0:
                    perfil_form.save()
                    mensaje = (True , 'El registro se realizo correctamente')
                else:
                    mensaje = (True , 'El Usuario ya es un administrador')
            else:
                mensaje = (True , 'El preregistro ya fue realizado')
        else:
            print(perfil_form.errors)
            mensaje = (True , 'ocurrio un error en el registro')

    countries = Country.objects.all().order_by('name')
    template = loader.get_template('formularioAdm.html')
    ctx = { 'mensaje': mensaje,
            'paises' : countries,
    }   
    return HttpResponse(template.render(ctx,request))