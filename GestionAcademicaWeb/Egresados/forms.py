from django.contrib.auth.forms import UserCreationForm
from django import forms
#from django.contrib.auth.models import Usuarios
from django.forms import fields, models, ModelForm, widgets
from .models import Usuarios
 

#Formulario para egresados
class FormEgresados(forms.ModelForm):
    '''nombre = forms.CharField(label="Nombre ", required=True)
    Appellidos = forms.CharField(label="Apellidos ", max_length=70, required=True)   
    #AppellidoMat = forms.CharField(label="Apellido materno ", required=True)
    email = forms.EmailField(label="E-mail ", max_length=50, required=True)
    Matricula = forms.IntegerField(label="Matricula ", required=True)
    Nombre = forms.CharField(label="Nombre ", required=True)
    Apellidos = forms.CharField(label="Apellidos ", max_length=70, required=True)
    email = forms.EmailField(label="E-mail ", max_length=50, required=True)
    fechaDeEgreso = forms.DateField(label="Fecha de egreso", required=True) 
    
    Matricula = forms.IntegerField(label="Matricula ", required=True)
    Nombre = forms.CharField(label="Nombre ", required=True)
    Apellidos = forms.CharField(label="Apellidos ", max_length=70, required=True)
    Email = forms.EmailField(label="E-mail ", max_length=50, required=True)
    '''
    class Meta:
        model = Usuarios
        fields = ['Matricula','Nombre','Apellidos','Email',]
        help_texts = {i:"" for i in fields }
        labels = {
            'Matricula':'Matricula',
            'Nombre':'Nombre',
            'Apellidos':'Apellidos',
            'Email':'Correo Electrónico',
        }
        widgets = {
            'Matricula': forms.TextInput(
                attrs = {
                'class': 'form-control',
                'placeholder': 'Matricula...'
                }
            ),
            'Nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Nombre...'
                }
            ),
            'Apellidos': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Apellidos...'
                }
            ),
            'Email': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Correo electrónico...'
                }
            )

        }
        #ºsucces_url = 
        

#Formulario para hacer login                 premium026@gmail.com
class UserLogin(forms.ModelForm):
    #campo para capturar el email y el parametro "widget" para establecer el diseño de los campos
    '''Email = forms.EmailField( max_length=50, 
    required=True, 
    widget=forms.EmailInput( 
        attrs =  {'class':'form-control', 'placeholder': 'E-mail...'}
                        ))'''

    #campo para capturar la contraseña y el parametro "widget" para establecer el diseño de los campos
    password = forms.CharField( 
    widget=forms.PasswordInput(
    attrs =  {'class':'form-control', 'placeholder': 'Password...'}
    ))

    class Meta:
        model = Usuarios
        fields = ["Email","password"]

        widgets = {
            'Email': forms.EmailInput(
                attrs = {
                'id': 'None',
                'class': 'form-control',
                'placeholder': 'Email...',
                'style':'bolder'
                }
            )
        }
            
        