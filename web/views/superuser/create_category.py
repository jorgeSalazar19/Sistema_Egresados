from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from domain.models import Category
from django.contrib.auth.models import User

def CreateCategory(request):

    if request.method == 'GET':
        username = request.GET.get('username')
        usuario = User.objects.filter(username=username)
        usuario = usuario[0]

    if request.method == 'POST':
        username = request.GET.get('username')
        usuario = User.objects.filter(username=username)
        usuario = usuario[0]
        nombre_categoria = request.POST.get('name_category')
        descripcion_categoria = request.POST.get('description_category')
    
    error = (False,'')
    template = loader.get_template('Root/CrearCategoria.html')
    ctx = {
            'error' : error,
            'usuario' : usuario,
    }
    return HttpResponse(template.render(ctx,request))
