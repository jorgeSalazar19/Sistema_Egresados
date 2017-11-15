from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Admin
from domain.models import Country
from django.core.validators import RegexValidator
import re

patron_nombre_apellido = re.compile('([A-ZÁÉÍÓÚ a-zñáéíóú]{1}[a-zñáéíóú A-ZÁÉÍÓÚ ]+[\s]*)+')
patron_email = re.compile('[\w]+@{1}[\w]+(\.[\w]+)*\.[a-z]{2,3}')
patron_dni = re.compile('[\d]{10}')
patron_telefono = re.compile('[3]{1}[0|1|2]{1}[\d]{8}')

def EditInfoAdm(request):
    error = (False , '')

    if request.method == 'GET':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)

        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('Admin/editarInfoAdm.html')
        else:
            return redirect('/login_admin')

    mensajes_error = []
    if request.method == 'POST':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)
        usuario = usuario[0]
        
        email = request.POST.get('email')
        country = request.POST.get('country')
        cellphone = request.POST.get('cellphone')

        if len(email) != 0 and re.match(patron_email,email) is not None:
            usuario.user.email = email
            usuario.user.save()

        else:
            error = "tienes un error en el campo email"
            mensajes_error.append(error)
            error = (True , mensajes_error)

        if len(country) != 0:
            country = Country.objects.get(id=country)
            usuario.country = country
            usuario.save()

        if len(cellphone) != 0:
            usuario.cellphone = cellphone
            usuario.save() 

        if len(request.FILES) != 0:
            profile_picture =  request.FILES['profile_picture']
        else:
            profile_picture = None

        if profile_picture is not None:
            usuario.profile_picture.delete()
            usuario.profile_picture = profile_picture
            usuario.save()
            mensaje = (True ,'Imagen cargada correctamente')

    print(error)
    paises = Country.objects.all().order_by('name')
    template = loader.get_template('Admin/editarInfoAdm.html')
    ctx = { 
        'mensaje' : error,
        'usuario' : usuario,
        'paises' : paises,
    }
    return HttpResponse(template.render(ctx,request))
