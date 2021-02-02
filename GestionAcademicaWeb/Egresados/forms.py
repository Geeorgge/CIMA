 
from django.db.models import fields
from django.db.models.enums import TextChoices
from Egresados.models import Opcion 
from django import forms
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput, Select
from django.shortcuts import redirect
from django.views.generic.edit import FormView
#from django.contrib.auth.models import Usuarios
#from django.forms import fields, models, ModelForm, widgets
 
'''Los valores de las respuestas son: 
1.- Insatisfactorio.                        2.- Poco satisfactorio. 
3.- Ni satisfactorio ni insatisfactorio     4.- Satisfactorio.       
5.- Muy satisfactorio.                      0 = como opción para cuando el alumno desconoce el servicio.'''

 
class EncuestaEgresados(forms.ModelForm):
    
    class Meta:
        model = Opcion
        fields = ['opciones']
        widgets = {
            'opciones' : forms.Select(attrs={'class': 'form-control' }),
        }

    #Funcion para quitar el "Label" del template
    def __init__(self, *args, **kwargs):
        super(EncuestaEgresados, self).__init__(*args, **kwargs)
        
        self.fields['opciones'].label = ""


     
         
         