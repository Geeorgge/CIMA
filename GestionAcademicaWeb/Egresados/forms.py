 
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
1.- Insatisfactorio. 2.- Poco satisfactorio. 3.- Ni satisfactorio ni insatisfactorio 
4.- Satisfactorio. 5.- Muy satisfactorio.
0 = como opción para cuando el alumno desconoce el servicio.'''

 
