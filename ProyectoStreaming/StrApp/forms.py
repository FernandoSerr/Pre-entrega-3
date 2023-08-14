from django import forms
from .models import Pelicula, Serie, Plataforma

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('titulo', 'genero', 'director')

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ('titulo', 'genero', 'temporadas')

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = ('nombre', 'suscripcion')

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)