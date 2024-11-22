from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Box(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.box} - {self.fecha} ({self.hora_inicio}-{self.hora_fin})"
