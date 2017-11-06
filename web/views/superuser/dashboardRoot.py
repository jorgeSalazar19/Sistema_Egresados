from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from domain.models import PreRegisterAdmin , Admin

from ...services import UserService
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User


def DashboardRoot(request):
    mensaje = (False,'')

    if request.method == 'GET':
        username = request.GET.get('username')
        usuario = User.objects.filter(username=username)

        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('DashBoardRoot.html')
            ctx = { 'mensaje': mensaje,
            'usuario' : usuario,
            }   
            return HttpResponse(template.render(ctx,request))
        else:
            return redirect('/login_admin')


