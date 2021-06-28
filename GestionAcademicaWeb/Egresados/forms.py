 
from django.db.models import fields
from django.db.models.enums import TextChoices
from Egresados.models import CustomUsuarios, Encuesta 
from django import forms
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput, Select
from django.shortcuts import redirect
from django.views.generic.edit import FormView
#from django.contrib.auth.models import Usuarios
from django.forms import fields, models, ModelForm, widgets

#       Modulo "forms.py" para implementar formularios de la app "Egresados"
 
'''Los valores de las respuestas son: 
1.- Insatisfactorio.                        2.- Poco satisfactorio. 
3.- Ni satisfactorio ni insatisfactorio     4.- Satisfactorio.       
5.- Muy satisfactorio.                      0 = como opción para cuando el alumno desconoce el servicio.'''

#Clase que implementa el formulario de la encuesta  
class EncuestaEgresados(forms.ModelForm):
    
    class Meta:
        model = Encuesta #Se usa el modelo "Encuesta"
        fields = [ 'values'] #Se usa el campo "values" del modelo "Encuesta"
        widgets = {  #Propiedad que añade estilos a los campos

            # 'asignatura' : forms.TextInput(attrs={'class': 'form-control' }),
            # 'option'     : forms.TextInput(attrs={'class': 'form-control' }),
            'values'     : forms.Select(attrs={'class': 'form-control' }),
        }


    #Funcion para quitar el "Label" del template
        #esta función es para añadir o editar estilos 
    def __init__(self, *args, **kwargs):
        super(EncuestaEgresados, self).__init__(*args, **kwargs)
        
        self.fields['values'].label = ""
         
    #Cambia el estatus del usuario cuando se envia la encuesta
    def user_status(self, commit=True):
        user = super(EncuestaEgresados, self).user_status(commit=False)

        pass
         
         