from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Admin
from domain.models import Country

def EditInfoAdm(request):
    mensaje = (False,'')

    if request.method == 'GET':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)

        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('Admin/editarInfoAdm.html')
        else:
            return redirect('/login_admin')

    if request.method == 'POST':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)
        usuario = usuario[0]
        
        email = request.POST.get('email')
        country = request.POST.get('country')
        cellphone = request.POST.get('cellphone')

        if len(email) != 0:
            usuario.user.email = email
            usuario.user.save()
        
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
        else:
            mensaje = (True, 'No se cargo')

    paises = Country.objects.all().order_by('name')
    template = loader.get_template('Admin/editarInfoAdm.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario,
        'paises' : paises,
    }
    return HttpResponse(template.render(ctx,request))
