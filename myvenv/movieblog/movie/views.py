from django.shortcuts import render ,get_object_or_404

from .models import Movies

def movie_list(request):
    movies = Movies.objects.all()
    return render(request, 'movie_list.html', {'Movies': movies})

def moduna_gore(request):

    romantik_movies = Movies.objects.filter(tür='Romantik')
    dram_movies = Movies.objects.filter(tür='Dram')
    bilim_movies = Movies.objects.filter(tür='Bilim Kurgu')
    komedi_movies = Movies.objects.filter(tür='Komedi')
    gerilim_movies = Movies.objects.filter(tür='Gerilim')
    korku_movies = Movies.objects.filter(tür='Korku')
    aksiyon_movies = Movies.objects.filter(tür='Aksiyon')

    modlar ={
      
        'romantik_movies': romantik_movies,
        'dram_movies' :dram_movies,
        'bilim_movies' :bilim_movies,
        'komedi_movies' :komedi_movies,
        'gerilim_movies' :gerilim_movies,
        'korku_movies' :korku_movies,
        'aksiyon_movies' :aksiyon_movies,

    }
    
    return render(request, 'moduna_gore.html' , modlar)

def anasayfa(request):

    latest_movies = Movies.objects.order_by('-yıl')[:6]
   
    context = {'latest_movies': latest_movies}
    
    return render(request, 'anasayfa.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movies, pk=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})



