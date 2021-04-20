from django.urls import path
from . import views

app_name = 'webcomic'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:language>/<int:episode>/<int:page>/', views.select, name='select'),
]