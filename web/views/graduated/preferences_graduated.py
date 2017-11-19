from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Category,Graduated,Activity
from django.contrib.auth.models import User

def PreferencesGraduated(request):
    mensaje = (False,'')
    dni = request.GET.get('dni')
    usuario = Graduated.objects.get(dni=dni)
    
    if request.method == 'POST':
        ids_categoria = request.POST.getlist('categorias')    
        categorias = []*len(ids_categoria)
        for i in range(len(ids_categoria)):
            id=ids_categoria[i]
            categoria = Category.objects.get(id=id)
            categorias.append(categoria)

        if len(categorias) != 0:
            usuario.preferences = categorias
            usuario.save()
            print(request.user.is_authenticated())
            redirect_authenticated_user=True
            return redirect('/dashboard_egresado?username='+dni)

        else :
            mensaje = (True , "Por favor seleccione por lo menos una categoria como preferencia")
            


    template = loader.get_template('Egresado/preferencias.html')
    categorias = Category.objects.all().order_by('name')
    ctx = { 'mensaje': mensaje,
            'categorias' : categorias,
    }   
    return HttpResponse(template.render(ctx,request))