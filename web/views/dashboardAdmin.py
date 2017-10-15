from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from domain.models import PreRegisterGraduated


def DashboardAdmin(request):
    mensaje = (False,'')

    if request.method == 'POST':
        Action_button = request.POST.get('tipo')
        id_pregister , action = Action_button.split()
        print("id : " , id_pregister , "accion : " , action)

        if action == "Aceptar":
            new_user = PreRegisterGraduated.objects.get(id=id_pregister)
            print(new_user.career)
        if action == "Eliminar":
            print("eliminar")

    if request.user is None or not request.user.is_authenticated():
        return redirect('/login_admin')
    

    template = loader.get_template('aceptarCuentas.html')
    pre_registros = PreRegisterGraduated.objects.all()
    ctx = { 'mensaje': mensaje,
            'pre_registros': pre_registros,
    }   
    return HttpResponse(template.render(ctx,request))