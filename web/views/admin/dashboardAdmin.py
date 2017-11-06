from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from domain.models import PreRegisterGraduated , Graduated , Admin

from ...services import UserService
from django.core.mail import EmailMessage
from django.conf import settings

def DashboardAdmin(request):
    mensaje = (False,'')
    if request.method == 'GET':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)

        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('DashBoardAdmin.html')
            pre_registros = PreRegisterGraduated.objects.all()
            ctx = { 'mensaje': mensaje,
            'pre_registros': pre_registros,
            'usuario' : usuario,
            }   
            return HttpResponse(template.render(ctx,request))
        else:
            return redirect('/login_admin')
    
