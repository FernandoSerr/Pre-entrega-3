from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    director = models.CharField(max_length=50)

class Serie(models.Model):
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    temporadas = models.IntegerField()

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    suscripcion = models.FloatField()