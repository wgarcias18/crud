from django.db import models

# Create your models here.

class Tareas(models.Model):
    titulo = models.CharField(max_length=1000)
    descripcion  = models.TextField(blank=True)

