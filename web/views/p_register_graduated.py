from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from web.forms import RegisterFormGraduated
from domain.models import Career
from domain.models import Country


def PreRegisterGraduated(request):
    mensaje = (False,'')
    if request.method == 'POST':
        perfil_form = RegisterFormGraduated(data=request.POST)
        print(request.POST)
        print(perfil_form.is_valid())
        if perfil_form.is_valid():
            perfil_form.save()
            mensaje = (True , 'El registro se realizo correctamente')
        else:
            print(perfil_form.errors)
            mensaje = (True , 'ocurrio un error en el registro')

    template = loader.get_template('formularioEgresado.html')
    careers = Career.objects.all()
    countries = Country.objects.all().order_by('name')
    print(countries)
    ctx = {
            'mensaje' : mensaje,
            'carreras' : careers,
            'paises' : countries,
    }   
    return HttpResponse(template.render(ctx,request))

