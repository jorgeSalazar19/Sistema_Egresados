from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from web.forms import UploadImageForm
from domain.models import Admin

def EditInfoAdm(request):
    mensaje = (False,'')

    if request.method == 'GET':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)

        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('Admin/editarInfoAdm.html')

    if request.method == 'POST':
        if len(request.FILES) != 0:
            profile_picture =  request.FILES['profile_picture']
        else:
            profile_picture = None
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)
        usuario = usuario[0]
        if profile_picture is not None:
            usuario.profile_picture.delete()
            usuario.profile_picture = profile_picture
            usuario.save()
            mensaje = (True ,'Imagen cargada correctamente')
        else:
            mensaje = (True, 'No se cargo')

    template = loader.get_template('Admin/editarInfoAdm.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario
    }
    return HttpResponse(template.render(ctx,request))
