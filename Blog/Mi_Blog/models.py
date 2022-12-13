from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jefe(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    sueldo = models.IntegerField()
    email = models.EmailField('', null=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Sueldo: {self.sueldo}, ID: {self.id}'

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    sueldo = models.IntegerField()
    email = models.EmailField('', null=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Sueldo: {self.sueldo}, ID: {self.id}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField('', null=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, ID: {self.id}'
    
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return f'User: {self.user}, Imagen: {self.imagen}'