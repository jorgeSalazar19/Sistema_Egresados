from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from web.forms import CreateFormCategory

from domain.models import Category
from django.contrib.auth.models import User

def DeleteCategory(request):
    mensaje = (False,'')
    usuario = []
    categorias = Category.objects.all()
    if request.method == 'GET':
        username = request.GET.get('username')
        id_category = request.GET.get('id_categoria')
        if username != None:
            username = username
        if id_category != None:
            id_categoria = id_category
        else:
            id_categoria = 0
        usuario = User.objects.filter(username=username)
        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            if id_categoria != 0:
                category = Category.objects.get(id=id_categoria)
                mensaje = (True,"Categoria "+ category.name +" Eliminada")
                category.delete()
                return redirect('/delete_categorias?username='+username)
                
        else:
            return redirect('/')


    template = loader.get_template('Root/eliminarCategorias.html')
    ctx = {
            'mensaje' : mensaje,
            'usuario' : usuario,
            'categorias' : categorias,
    }
    return HttpResponse(template.render(ctx,request))