from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Graduated ,  Country , Category

def EditInfoGra(request):
    mensaje = (False,'')
    if request.method == 'GET':
        dni = request.GET.get('username')
        usuario = Graduated.objects.filter(dni=dni)

        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('Egresado/editarInfo.html')

    if request.method == 'POST':
        dni = request.GET.get('username')
        usuario = Graduated.objects.filter(dni=dni)
        usuario = usuario[0]

        email = request.POST.get('email')
        id_country = request.POST.get('country')
        ids_categoria = request.POST.getlist('categorias') 

        categorias = []*len(ids_categoria)
        for i in range(len(ids_categoria)):
            id=ids_categoria[i]
            categoria = Category.objects.get(id=id)
            categorias.append(categoria)

        if len(categorias) != 0:
            usuario.preferences = categorias
            usuario.save()
        else:
            mensaje = (True , "Debes seleccionar almenos una categoria para tus preferencias")

        if len(email) != 0:
            usuario.user.email = email
            usuario.user.save()

        if len(id_country) != 0:
            country = Country.objects.get(id__exact=id_country)
            usuario.country = country
            usuario.save()
        if len(request.FILES) != 0:
            profile_picture =  request.FILES['profile_picture']
        else:
            profile_picture = None

        if profile_picture is not None:
            usuario.profile_picture.delete()
            usuario.profile_picture = profile_picture
            usuario.save()

        return redirect('/success_profile_edition_graduated?username='+dni)
    paises = Country.objects.all().order_by('name')
    categoria_g = usuario.preferences.all()
    print(categoria_g)
    categorias = Category.objects.all().order_by('name')
    template = loader.get_template('Egresado/editarInfo.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario,
        'paises' : paises,
        'categorias' : categorias,
        'categoria_g' : categoria_g,
    }
    return HttpResponse(template.render(ctx,request))