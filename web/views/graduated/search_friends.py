from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Graduated
from django.contrib.auth.models import User

def Search(request):
    usuario = 0
    historial = 0
    usuarios = []
    usuarios_encontrados = []
    encontrados = []
    mensaje = (False , "")

    if request.method == 'GET':
        username = request.GET.get('username')
        dni = request.GET.get('dni')
        usuario = Graduated.objects.filter(dni__exact=username)
        usuario = usuario[0]

    if request.method == 'POST':
        name = request.POST.get('nombre')
        username = request.GET.get('username')
        dni = request.GET.get('dni')
        Egresados = Graduated.objects.all()
        usuarios = User.objects.filter(first_name__contains=name.capitalize()).exclude(username__exact=username)
        print(len(usuarios))
        if len(usuarios) == 0:
            mensaje = (True , "No hemos encontrado ningun usuario con ese nombre")

        for usuario in usuarios:
            for Egresado in Egresados: 
                if str(usuario.username) == str(Egresado.dni):
                    usuarios_encontrados.append(usuario)
        usuario = Graduated.objects.filter(dni__exact=username)
        usuario = usuario[0]

        amigos = usuario.friends.all().exclude(dni__exact=username)

        encontrados = []
        for usuario_e in usuarios_encontrados:
            if usuario_e in amigos:
                pass
            else:
                encontrados.append(usuario_e)

    template = loader.get_template('Egresado/searchFriend.html')
    ctx = { 
            'usuario' : usuario,
            'usuarios' : encontrados,
            'mensaje' : mensaje
    }   
    return HttpResponse(template.render(ctx,request))