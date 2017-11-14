from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from domain.models import Admin , Graduated
from domain.models import Category,Activity
from web.forms import CreateFormActivity

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.conf import settings

def CreateActivity(request):
    mensaje = (False,'')
    mensaje_only = (False,"")
    usuario = []

    if request.method == 'GET':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)
        if len(usuario) != 0 and request.user.is_authenticated():
            usuario = usuario[0]
            template = loader.get_template('Admin/crearActividades.html')
        else:
            return redirect('/login_admin')

    if request.method == 'POST':
        dni = request.GET.get('dni')
        usuario = Admin.objects.filter(dni=dni)
        name_activity = request.POST.get('name')
        usuario = usuario[0]
        categoria_p = request.POST.get('category')
        actividad = request.POST.get('name')
        form_activity = CreateFormActivity(data=request.POST , files=request.FILES)
        actividades = Activity.objects.all()

        if form_activity.is_valid():
            name = form_activity.cleaned_data['name']
            description = form_activity.cleaned_data['description']

            error = []
            for actividad in actividades:
                print (actividad.name , name_activity)
                if (str(actividad.name).lower()) == (str(name_activity).lower()):
                    error.append(actividad)
                    mensaje_only = (True,"Actividad ya existe")
            if len(error) == 0: 
                form_activity.save()
                mensaje_only = (True , "Actividad guardada full")
                egresados = Graduated.objects.all()
                to_list = []
                for egresado in egresados:
                    categorias = egresado.preferences.all()
                    for categoria in categorias:
                        if str(categoria.id) == str(categoria_p):
                            email = egresado.user.email
                            to_list.append(email)

                to_list.append(settings.EMAIL_HOST_USER)
                from_email = settings.EMAIL_HOST_USER
                current_site = get_current_site(request)
                SendMail(from_email,to_list,current_site,actividad)
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
        'mensaje_o' : mensaje_only,
    }
    return HttpResponse(template.render(ctx,request))


def SendMail(fromEmail,to_list,current_site,actividad):
    subject, from_email, to = 'Sistema Egresados -- Actividad de interes', fromEmail, to_list
    message = render_to_string('FormatosCorreo/FormatoCreateAct.html', {
        'domain' : current_site.domain,
        'actividad' : actividad
        })
    email = EmailMessage(subject, message, from_email, to)
    email.send()