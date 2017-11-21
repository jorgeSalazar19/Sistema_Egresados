from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from web.forms import RegisterFormGraduated
from domain.models import Career
from domain.models import Country , PreRegisterGraduated as PreRegister , Graduated


def PreRegisterGraduated(request):
    mensaje = (False,'' , False)
    datos = []
    if request.method == 'POST':
        id_pregister = request.POST.get('dni')
        email_preregister = request.POST.get('email')
        usuario_dni = PreRegister.objects.filter(dni=id_pregister)
        usuario_email = PreRegister.objects.filter(email=email_preregister)
        usuario_graduated = Graduated.objects.filter(dni=id_pregister)
        perfil_form = RegisterFormGraduated(data=request.POST)
        datos = request.POST
        if perfil_form.is_valid():
            if len(usuario_dni) == 0 and len(usuario_email) == 0:
                if len(usuario_graduated) == 0:
                    name = perfil_form.cleaned_data['first_name']
                    last_name = perfil_form.cleaned_data['last_name']
                    email = perfil_form.cleaned_data['email']
                    dni = perfil_form.cleaned_data['dni']
                    graduation_year = perfil_form.cleaned_data['graduation_year']
                    
                    
                    perfil_form.save()
                    return redirect('/register_done')
                else:
                    mensaje = (True , 'El Usuario ya es un Egresado' , True)
                    
            else:
                mensaje = (True , 'EL preregistro ya fue realizado', True)
        else:
            errors = perfil_form.get_errors()
            print(errors)
            message_e = []
            for error in errors:
                message_e.append(str(perfil_form.errors[error]))
            mensaje = (True , message_e, False)
            errors = perfil_form.clean_errors()


    template = loader.get_template('Egresado/formularioEgresado.html')
    careers = Career.objects.all().order_by('name')
    countries = Country.objects.all().order_by('name')
    ctx = {
            'mensaje' : mensaje,
            'carreras' : careers,
            'paises' : countries,
            'datos' : datos,
    }   
    return HttpResponse(template.render(ctx,request))

