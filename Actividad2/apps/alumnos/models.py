from django.db import models

# Create your models here.

class alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    carrera = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre