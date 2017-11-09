from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

def EditInfoAdm(request):
    template = loader.get_template('Admin/editarInfoAdm.html')
    ctx = {}
    return HttpResponse(template.render(ctx,request))