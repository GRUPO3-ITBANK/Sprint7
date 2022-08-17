from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractUser)

# Create your models here.
class ClienteManager(BaseUserManager):
    def create_user(self, DNI, nombre, apellido,fecha_de_nac,tipo_cliente, password=None):
        if not DNI:
            raise ValueError('Hola, debes ingresar DNI')
        user = self.model(
            DNI=DNI,
            nombre=nombre,
            apellido=apellido,
            fecha_de_nac=fecha_de_nac,
            tipo_cliente=tipo_cliente
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, DNI, nombre,apellido,fecha_de_nac,tipo_cliente, password=None):
        user = self.create_user(
            DNI,
            password=password,
            nombre=nombre,
            apellido=apellido,
            fecha_de_nac=fecha_de_nac,
            tipo_cliente=tipo_cliente
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Cliente(AbstractUser):
    DNI=models.IntegerField('DNI',unique=True,)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_de_nac=models.DateField()
    tipo_cliente = models.CharField(default="Classic",max_length=50)

    objects = ClienteManager()

    USERNAME_FIELD = 'DNI'
    REQUIRED_FIELDS = ['nombre','apellido','fecha_de_nac','tipo_cliente']

    def __str__(self):
        return self.DNI
