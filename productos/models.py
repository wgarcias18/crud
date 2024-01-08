from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=1000)
    codigo  = models.TextField(blank=True)
    precio = models.TextField(blank=True)
    cantidad = models.TextField(blank=True)
    marca = models.TextField(blank=True)
