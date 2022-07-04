from django.shortcuts import render
from .models import *


def index(request):
    directores = Director.objects.all()

    return render(request, 'index.html', context={'directores': directores})


def info_director(request, id):
    director = Director.objects.get(id=id)
    peliculas = director.pelicula_set.all()

    context = {
        'director': director,
        'peliculas': peliculas
    }
    return render(request, 'info_director.html', context=context)

def info_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.duracion = formatear_duracion(pelicula.duracion)

    return render(request, 'info_pelicula.html', context={"pelicula": pelicula})


def formatear_duracion(duracion):
    horas = 0
    minutos = 0

    if duracion > 60:
        horas = duracion // 60
        minutos = duracion % 60

    return f'{horas}h {minutos}min'