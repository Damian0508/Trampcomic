# from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    response = redirect('/pl/1/0')
    return response

def select(request, language, episode, page):
    path_str = '/media/'
    if language == 'pl':
        path_str += 'PL_'
    else:
        path_str += 'EN_'
    
    path_str += f'{episode}_{page}.png'

    return render(request, "webcomic/index.html", {'path': path_str, 'episode': episode, 'page': page})

