from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="directores"),
    path('director/<int:id>', views.info_director, name='info_director'),
    path('pelicula/<int:id>', views.info_pelicula, name='info_pelicula'),
]