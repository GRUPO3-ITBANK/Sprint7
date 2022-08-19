from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    
    email = models.EmailField(verbose_name='mail address',max_length=255)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    DNI=models.CharField(max_length=50,unique=True,)
    fecha_de_nac=models.DateField()
    TIPOS=(
        ('C','Classic'),
        ('G','Gold'),
        ('B','Black')
    )
    tipo_cliente = models.CharField(max_length=1,choices=TIPOS)
    
    def __str__(self):
        return "DNI " + self.DNI +": "+ self.nombre +" "+  self.apellido

    class Meta:
        db_table = 'Clientes'




