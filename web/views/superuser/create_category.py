from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from domain.models import Category 

def CreateCategory(request):


    if request.method == 'POST':
        nombre_categoria = request.POST.get('name_category')
        descripcion_categoria = request.POST.get('description_category')
        print(nombre_categoria,descripcion_categoria)
    
    error = (False,'')
    template = loader.get_template('Root/CrearCategoria.html')
    ctx = {
            'error' : error,
    }
    return HttpResponse(template.render(ctx,request))
