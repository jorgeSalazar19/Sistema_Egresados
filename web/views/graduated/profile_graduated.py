from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Graduated

def ProfileGraduated(request):

    if request.method == 'GET':
        dni = request.GET.get('username')
        usuario = Graduated.objects.filter(dni=dni)
        usuario = usuario[0]

        preferencias = usuario.preferences.all()
        print(preferencias)
        for preferencia in preferencias:
            print(preferencia.name)
        template = loader.get_template('Egresado/perfilEgresado.html')
        ctx = {
            'usuario' : usuario,
            'categoria_g' : preferencias
        }

        return HttpResponse(template.render(ctx,request))