from typing import get_args
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
#from django.contrib.auth.models import Usuarios
from django.forms import fields, models, ModelForm, widgets
from .models import CustomUsuarios
 
 

#Formulario para egresados
class FormEgresados(forms.ModelForm):
    
    class Meta:
        model = CustomUsuarios
        fields = ['matricula','username','last_name','email',]
        widgets = {
            'matricula': forms.NumberInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }

        
        
        
        

#Formulario para login                 premium026@gmail.com
class UserLogin(forms.ModelForm):
    #password = forms.PasswordInput()
    password = forms.CharField( 
    widget=forms.PasswordInput(
    attrs =  {'class':'form-control', 'placeholder': 'Password...'}
    ))
    #campo para capturar la contraseña y el parametro "widget" para establecer el diseño de los campos
    #El campo de "EMAIL" lo tomamos del modelo "Usuarios"'''
     
     
    class Meta:
        model = CustomUsuarios
        fields = ["email", "password"]

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        