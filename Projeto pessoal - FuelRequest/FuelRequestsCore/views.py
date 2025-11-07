from django.shortcuts import render, get_object_or_404
from . import models as cr

from django.http import HttpResponse

from django.template import loader


def index(request):
    todos_os_planos = cr.plano.objects.all()
    context = {
        'planos': todos_os_planos
    }
    return render(request, 'index.html', context)

def ver_plano(request, pk):
    plans = get_object_or_404(cr.plano,id=pk)
    #plans = cr.plano.objects.get(id=pk)
    context={
        'plano': plans}
    return render(request, 'plano.html', context)


def contato(request,pk):
    return render(request, 'contato.html')


def error404(request, exception):
    template = loader.get_template('error404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request, exception):
    template = loader.get_template('error500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)