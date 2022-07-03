from django.db import models

# Create your models here.
class Director(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateField(null=False)
    fecha_fallecimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'


class Pelicula(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    snopsis = models.TextField(max_length=200, null=True)
    lanzamiento = models.DateField(null=False)
    duracion = models.PositiveIntegerField(null=False, help_text='Duración en Minutos')
    director = models.ManyToManyField(Director)

    def __str__(self):
        return self.titulo
