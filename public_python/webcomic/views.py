from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Episode, Page


def nr_of_episode_pages(episode, ep_lang_str):
    try:    
        selected_episode = Episode.objects.get(name=f'{ep_lang_str}{episode}')
        nr_of_pages = Page.objects.filter(episode=selected_episode).count()
    except:
        nr_of_pages = 1
    return nr_of_pages


def get_page_url(episode, page, ep_lang_str):
    nr_of_pages = nr_of_episode_pages(episode, ep_lang_str)
    if page > nr_of_pages - 1:
        page = 0
        episode += 1
    try:
        comic_page = Page.objects.get(name=f'{ep_lang_str}{episode}_{page}.png')
    except:
        comic_page = Page.objects.get(name=f'{ep_lang_str}404.png')
    page_url = comic_page.image.url
    return page_url


def controller(episode, page, ep_lang_str):
    
    nr_of_episodes = Episode.objects.filter(counted=True).count()
    if episode > nr_of_episodes:
        episode = 1
    if episode <  1:
        episode = nr_of_episodes
    
    nr_of_pages = nr_of_episode_pages(episode, ep_lang_str)
    if page > nr_of_pages - 1:
        page = 0
        episode += 1
    if page < 0:
        if episode > 1:
            episode -= 1
            nr_of_pages = nr_of_episode_pages(episode, ep_lang_str)
            page = nr_of_pages - 1
        else:
            page = 0
    nr_of_pages = nr_of_episode_pages(episode, ep_lang_str)

    try:
        comic_page = Page.objects.get(name=f'{ep_lang_str}{episode}_{page}.png')
    except:
        comic_page = Page.objects.get(name=f'{ep_lang_str}404.png')
    path_str = comic_page.image.url
    return episode, page, nr_of_pages, path_str


def index(request):
    response = redirect('/pl/1/0')
    return response


def select(request, language, episode, page):
    if language == 'pl':
        ep_lang_str = 'PL_'
        url_str = '/pl/'
        hero_path = '/static/webcomic/images/pl_John.png'
    else:
        ep_lang_str = 'ENG_'
        url_str = '/en/'
        hero_path = '/static/webcomic/images/en_John.png'

    if request.is_ajax() and request.method == "GET":
        element_id = request.GET.get('element_id')
        if element_id == 'next-page':
            page += 1

        elif element_id == 'previous-page':
            page -= 1

        elif element_id == 'next-episode':
            episode += 1
            page = 0

        elif element_id == 'previous-episode':
            episode -= 1
            page = 0
        else:
            pass
        
        episode, page, nr_of_pages, path_str = controller(episode, page, ep_lang_str)
        next_images_path_dict = {}
        for number in range(1,5):
            next_images_path_dict[f'image{number}'] = \
                get_page_url(episode, page+number, ep_lang_str)

        url_str += f'{episode}/{page}/'

        return JsonResponse({'image_path': path_str, 'new_url': url_str,
            'episode':episode, 'page': page, 'nr_of_pages': nr_of_pages-1,
            'hero_path': hero_path,
            'next_images_path_dict': next_images_path_dict}, status=200)
    else:
        episode, page, nr_of_pages, path_str = controller(episode, page, ep_lang_str)
        next_images_path_dict = {}
        for number in range(1,5):
            next_images_path_dict[f'image{number}'] = \
                get_page_url(episode, page+number, ep_lang_str)
            
        if request.user_agent.is_mobile or request.user_agent.is_tablet:
            return render(request, "webcomic/mobile.html", {
                'image_path': path_str, 'episode': episode, 'page': page,
                'nr_of_pages': nr_of_pages-1, 'hero_path': hero_path,
                'next_images_path_dict': next_images_path_dict})
        else:
            return render(request, "webcomic/desktop.html", {
                'image_path': path_str, 'episode': episode, 'page': page,
                'nr_of_pages': nr_of_pages-1, 'hero_path': hero_path,
                'next_images_path_dict': next_images_path_dict})