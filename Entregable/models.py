from django.db import models

# Create your models here.

# ACA ES DONDE SE GENERAN LAS CLASES

class Destinos(models.Model):

    pais = models.CharField(max_length=25)
    ciudad = models.CharField(max_length=25)

    def __str__(self): 
        return f"{self.pais} - {self.ciudad}"

class Datos(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField (max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-mail: {self.email}"

class Calculo(models.Model):

    precio = models.FloatField(max_length=2)
    precio2 = models.FloatField(max_length=2)

    def __str__(self): 
        return f'{self.precio+self.precio2}'