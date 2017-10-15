from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from web.forms import RegisterFormAdmin


from domain.models import Country


def PreRegisterAdmin(request):
    mensaje = (False,'')
    if request.method == 'POST':
        perfil_form = RegisterFormAdmin(data=request.POST)
        if perfil_form.is_valid():
            perfil_form.save()
            mensaje = (True , 'El registro se realizo correctamente')
        else:
            print(perfil_form.errors)
            mensaje = (True , 'ocurrio un error en el registro')

    countries = Country.objects.all().order_by('name')
    template = loader.get_template('formularioAdm.html')
    ctx = { 'mensaje': mensaje,
            'paises' : countries,
    }   
    return HttpResponse(template.render(ctx,request))