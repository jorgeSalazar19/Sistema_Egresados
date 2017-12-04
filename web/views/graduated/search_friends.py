from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Graduated
from django.contrib.auth.models import User
from django.db.models import Q

def Search(request):
    usuario = 0
    historial = 0
    usuarios = []
    usuarios_encontrados = []
    encontrados = []
    mensaje = (False , "")
    usuario_agregar = None
    name = ''


    if request.method == 'GET':
        username = request.GET.get('username')
        dni_busqueda = request.GET.get('dni')
        usuario = Graduated.objects.filter(dni__exact=username)
        usuario = usuario[0]

        if dni_busqueda is not None:
            usuario_agregar = Graduated.objects.get(dni__exact=dni_busqueda)
            print(usuario_agregar)

        if usuario_agregar is not None:
            usuario.friends.add(usuario_agregar)
            mensaje = (True , "Se ha agregado correctamente al usuario " + usuario_agregar.user.first_name +" " + usuario_agregar.user.last_name)

    if request.method == 'POST':
        name = request.POST.get('nombre')
        username = request.GET.get('username')
        dni = request.GET.get('dni')
        Egresados = Graduated.objects.all()
        usuarios = User.objects.filter(Q(first_name__contains=name.capitalize())|Q(last_name__contains=name.capitalize())).exclude(username__exact=username)
        print(len(usuarios))


        for usuario in usuarios:
            for Egresado in Egresados: 
                if str(usuario.username) == str(Egresado.dni):
                    usuarios_encontrados.append(Egresado)
        usuario = Graduated.objects.filter(dni__exact=username)
        usuario = usuario[0]

        amigos = usuario.friends.all().exclude(dni__exact=username)

        encontrados = []
        for usuario_e in usuarios_encontrados:
            if usuario_e in amigos:
                pass
            else:
                encontrados.append(usuario_e)

        if len(encontrados) == 0:
            mensaje = (True , "No hemos encontrado ningun usuario con ese nombre")

    template = loader.get_template('Egresado/searchFriend.html')
    ctx = { 
            'usuario' : usuario,
            'usuarios' : encontrados,
            'mensaje' : mensaje,
            'name' : name
    }   
    return HttpResponse(template.render(ctx,request))