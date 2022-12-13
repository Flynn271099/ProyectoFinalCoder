from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AniadirEmpleado(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    sueldo = forms.IntegerField()
    email = forms.EmailField()
    
class AniadirJefe(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    sueldo = forms.IntegerField()

class AniadirCliente(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    
class SingUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        
class UserEditForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k: '' for k in fields}