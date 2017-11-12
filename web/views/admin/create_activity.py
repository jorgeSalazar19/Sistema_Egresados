from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Admin
from domain.models import Category
from web.forms import CreateFormActivity

def CreateActivity(request):
    mensaje = (False,'')
    usuario = []

    if request.method == 'GET':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)
        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('Admin/crearActividades.html')

    if request.method == 'POST':
        form_activity = CreateFormActivity(data=request.POST , files=request.FILES)
        if form_activity.is_valid():
            name = form_activity.cleaned_data['name']
            description = form_activity.cleaned_data['description']
            form_activity.save()
            mensaje = (True , "Categoria guardada full")
        else:
            errors = form_activity.get_errors()
            message_e = []
            for error in errors:
                message_e.append(str(form_activity.errors[error]))
            mensaje = (True , message_e)
            errors = form_activity.clean_errors()
            mensaje = (True , message_e)

    categories = Category.objects.all().order_by('name')
    template = loader.get_template('Admin/crearActividades.html')
    ctx = { 
        'mensaje' : mensaje,
        'usuario' : usuario,
        'categories' : categories,
    }
    return HttpResponse(template.render(ctx,request))