from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from domain.models import Graduated 

def SuccessSendMail(request):
    mensaje = (False,'')
    usuario = []

    if request.method == 'GET':
        username = request.GET.get('username')
        usuario = Graduated.objects.filter(dni=username)
        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('Egresado/correoEnviado.html')
        else:
            return redirect('/login_admin')

    template = loader.get_template('Egresado/correoEnviado.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario,
    }
    return HttpResponse(template.render(ctx,request))