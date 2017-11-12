from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

def RegisterDone(request):
    template = loader.get_template('Egresado/registroExitoso.html')
    ctx = { 
    }   
    return HttpResponse(template.render(ctx,request))