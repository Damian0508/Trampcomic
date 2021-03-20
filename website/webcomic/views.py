# from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "webcomic/index.html")

def select(request, language, episode, page, template_name="index.html"):
    path_str = 'kot'
    return render(request, template_name, {'path': path_str})

