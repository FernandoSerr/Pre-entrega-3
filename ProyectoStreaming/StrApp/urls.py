from django.urls import path
from . import views

urlpatterns = [
    path('peliculas/', views.agregar_pelicula, name='peliculas'),
    path('series/', views.agregar_serie, name='series'),
    path('plataformas/', views.agregar_plataforma, name='plataformas'),
    path('buscar/', views.buscar, name='buscar'),
]