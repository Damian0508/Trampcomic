from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    response = redirect('/pl/1/0')
    return response

def select(request, language, episode, page):
    path_str = '/media/'
    if language == 'pl':
        path_str += 'PL_'
        url_str = '/pl/'
    else:
        path_str += 'ENG_'
        url_str = '/en/'

    if request.is_ajax() and request.method == "GET":
        element_id = request.GET.get('element_id')
        max_episode = 2
        max_page = 45
        if element_id == 'next-page':
            page += 1
            if page > max_page:
                page = 0
                episode += 1

        elif element_id == 'previous-page':
            page -= 1
            if page < 0:
                page = max_page

        elif element_id == 'next-episode':
            episode += 1
            page = 0
            if episode > max_episode:
                episode = 1

        elif element_id == 'previous-episode':
            episode -= 1
            page = 0
            if episode <  1:
                episode = max_episode
        else:
            pass

        path_str += f'{episode}_{page}.png'
        url_str += f'{episode}/{page}/'

        return JsonResponse({'path': path_str, 'new_url': url_str, 'episode':episode, 'page': page}, status=200)
    else:
        path_str += f'{episode}_{page}.png'
        # return render(request, "webcomic/desktop.html", {'path': path_str, 'episode': episode, 'page': page})
        return render(request, "webcomic/mobile.html", {'path': path_str, 'episode': episode, 'page': page})
