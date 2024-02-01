from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('Filmler/',views.movie_list, name='movie_list'),
    path('moduna_gore/', views.moduna_gore, name='moduna_gore'),
    path('Anasayfa/', views.anasayfa, name='anasayfa'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail')
]


