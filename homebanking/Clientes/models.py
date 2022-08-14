from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    DNI=models.TextField(max_length=25)
    fecha_de_nac=models.DateField()