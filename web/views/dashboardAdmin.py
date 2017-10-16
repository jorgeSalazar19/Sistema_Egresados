from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from domain.models import PreRegisterGraduated , Graduated

from ..services import UserService
from django.core.mail import send_mail
from django.conf import settings

def DashboardAdmin(request):
    mensaje = (False,'')

    if request.method == 'POST':
        Action_button = request.POST.get('tipo')
        id_pregister , action = Action_button.split()
        print("id : " , id_pregister , "accion : " , action)
        preregister = PreRegisterGraduated.objects.get(id=id_pregister)
        if action == "Aceptar":
            user_data = preregister.__dict__
            user_data['temporal_password'] = get_random_string(length=12)
            user_service = UserService(user_data)
            user_service.register_graduated()
            print(user_data['temporal_password'])
            print(user_data['email'])

            subject = 'Tu Contraseña'
            message = 'Bienvenido al sistema de egresados esta es tu contraseña' + " " + user_data['temporal_password']
            from_email = settings.EMAIL_HOST_USER
            to_list = [user_data['email'],settings.EMAIL_HOST_USER]
            send_mail(subject,message,from_email,to_list,fail_silently=False) 

            
        if action == "Eliminar":
            print("eliminar")
            preregister.delete()

    if request.user is None or not request.user.is_authenticated():
        return redirect('/login_admin')
    
    template = loader.get_template('aceptarCuentas.html')
    pre_registros = PreRegisterGraduated.objects.all()
    ctx = { 'mensaje': mensaje,
            'pre_registros': pre_registros,
    }   
    return HttpResponse(template.render(ctx,request))