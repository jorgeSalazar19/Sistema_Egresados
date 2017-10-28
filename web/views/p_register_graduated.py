from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from web.forms import RegisterFormGraduated
from domain.models import Career
from domain.models import Country , PreRegisterGraduated as PreRegister , Graduated


def PreRegisterGraduated(request):
    mensaje = (False,'')
    if request.method == 'POST':
        id_pregister = request.POST.get('dni')
        email_preregister = request.POST.get('email')
        usuario_dni = PreRegister.objects.filter(dni=id_pregister)
        usuario_email = PreRegister.objects.filter(email=email_preregister)
        usuario_graduated = Graduated.objects.filter(dni=id_pregister)
        perfil_form = RegisterFormGraduated(data=request.POST)
        if perfil_form.is_valid():
            if len(usuario_dni) == 0 and len(usuario_email) == 0:
                if len(usuario_graduated) == 0:
                    name = perfil_form.cleaned_data['first_name']
                    last_name = perfil_form.cleaned_data['last_name']
                    email = perfil_form.cleaned_data['email']
                    dni = perfil_form.cleaned_data['dni']
                    birthday = perfil_form.cleaned_data['birthday']
                    graduation_year = perfil_form.cleaned_data['graduation_year']
                    perfil_form.save()
                    mensaje = (True , 'El registro se realizo correctamente')
                else:
                    mensaje = (True , 'El Usuario ya es un Egresado')
            else:
                mensaje = (True , 'EL preregistro ya fue realizado')
        else:
            print(perfil_form.errors)
            mensaje = (True , 'ocurrio un error en el registro')

    template = loader.get_template('formularioEgresado.html')
    careers = Career.objects.all()
    countries = Country.objects.all().order_by('name')
    ctx = {
            'mensaje' : mensaje,
            'carreras' : careers,
            'paises' : countries,
    }   
    return HttpResponse(template.render(ctx,request))

