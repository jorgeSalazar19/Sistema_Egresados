from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User

def SuccessCategory(request):
    mensaje = (False,'')
    usuario = []
    if request.method == 'GET':
        username = request.GET.get('username')
        usuario = User.objects.filter(username=username)
        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
        else:
            return redirect('/')
    template = loader.get_template('Root/categoriaCreada.html')
    ctx = {
            'mensaje' : mensaje,
            'usuario' : usuario,
    }
    return HttpResponse(template.render(ctx,request))