from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from web.forms import CreateFormCategory

from domain.models import Category
from django.contrib.auth.models import User

def ListCategory(request):
    mensaje = (False,'')
    usuario = []
    categorias = Category.objects.all()
    if request.method == 'GET':
        username = request.GET.get('username')
        usuario = User.objects.filter(username=username)
        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
        else:
            return redirect('/')
    template = loader.get_template('Root/listaCategorias.html')
    ctx = {
            'mensaje' : mensaje,
            'usuario' : usuario,
            'categorias' : categorias,
    }
    return HttpResponse(template.render(ctx,request))