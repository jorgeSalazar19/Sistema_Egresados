from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from web.forms import CreateFormCategory

from domain.models import Category
from django.contrib.auth.models import User

def CreateCategory(request):
    mensaje = (False,'')
    mensaje_only = (False , "")
    usuario = []
    datos = []
    if request.method == 'GET':
        username = request.GET.get('username')
        usuario = User.objects.filter(username=username)
        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
        else:
            return redirect('/')



    if request.method == 'POST':
        username = request.GET.get('username')
        usuario = User.objects.filter(username=username)
        usuario = usuario[0]
        name_category = request.POST.get('name')
        categorias = Category.objects.all()
        form_category = CreateFormCategory(data=request.POST)
        datos = request.POST

        error = []
        if form_category.is_valid():
            name = form_category.cleaned_data['name']
            description = form_category.cleaned_data['description']
            for categoria in categorias:
                if (str(categoria.name).lower()) == (str(name_category).lower()):
                    error.append(categoria)
                    mensaje_only = (True,"Categoria ya existe")
            if len(error) == 0: 
                form_category.save()
                mensaje_only = (True , "Categoria guardada full")
        else:
            errors = form_category.get_errors()
            message_e = []
            for error in errors:
                message_e.append(str(form_category.errors[error]))
            mensaje = (True , message_e)
            errors = form_category.clean_errors()
            mensaje = (True , message_e)

    

    template = loader.get_template('Root/CrearCategoria.html')
    ctx = {
            'mensaje' : mensaje,
            'usuario' : usuario,
            'mensaje_o' : mensaje_only,
            'datos' : datos,
    }
    return HttpResponse(template.render(ctx,request))
