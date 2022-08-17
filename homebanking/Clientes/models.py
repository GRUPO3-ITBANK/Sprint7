from xml.etree.ElementTree import tostring
from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractUser)

# Create your models here.
class ClienteManager(BaseUserManager):
    def create_user(self, DNI, email, nombre, apellido,fecha_de_nac,tipo_cliente, password=None):
        if not DNI:
            raise ValueError('Hola, debes ingresar DNI')
        user = self.model(
            DNI=DNI,
            email=self.normalize_email(email),
            nombre=nombre,
            apellido=apellido,
            fecha_de_nac=fecha_de_nac,
            tipo_cliente=tipo_cliente
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, DNI, email, nombre,apellido,fecha_de_nac,tipo_cliente, password=None):
        user = self.create_user(
            DNI,
            email=self.normalize_email(email),
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
    username=models.IntegerField(blank=True,null=True)
    def __init__(self,*args,**kwargs):
        super(Cliente, self).__init__(*args,**kwargs)
        if self.username is None:
            self.username = self.DNI
    email = models.EmailField(verbose_name='email address',max_length=255)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_de_nac=models.DateField()
    TIPOS=(
        ('C','Classic'),
        ('G','Gold'),
        ('B','Black')
    )
    tipo_cliente = models.CharField(max_length=1,choices=TIPOS)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = ClienteManager()

    USERNAME_FIELD = 'DNI'
    REQUIRED_FIELDS = ['email','nombre','apellido','fecha_de_nac','tipo_cliente']

    def __str__(self):
        return self.DNI

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
