from django.shortcuts import render, redirect
from .models import Pelicula, Serie, Plataforma
from .forms import PeliculaForm, SerieForm, PlataformaForm, BusquedaForm

# Create your views here.
def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'StrApp/peliculas.html', {'form': form})

def agregar_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('series')
    else:
        form = SerieForm()
    return render(request, 'StrApp/series.html', {'form': form})

def agregar_plataforma(request):
    if request.method == 'POST':
        form = PlataformaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plataformas')
    else:
        form = PlataformaForm()
    return render(request, 'StrApp/plataformas.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            peliculas = Pelicula.objects.filter(titulo__icontains=busqueda)
            return render(request, 'StrApp/resultados.html', {'peliculas': peliculas})
    else:
        form = BusquedaForm()
    return render(request, 'StrApp/buscar.html', {'form': form})