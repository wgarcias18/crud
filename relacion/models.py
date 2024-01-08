from django.db import models


# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=1000)
    estado  = models.TextField(blank=True)

class Prooveedor(models.Model):
    pais = models.ForeignKey(Pais, null=True,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=1000)
    estado  = models.TextField(blank=True)
    marca = models.TextField(blank=True)


class product(models.Model):
    prooveedor = models.ForeignKey(Prooveedor, null=True ,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=1000)
    marca = models.TextField(blank=True)
    precio = models.PositiveSmallIntegerField()
    valor = models.PositiveSmallIntegerField(blank=True)


