from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView 

#from django.forms.models import Usuarios
 


# Create your views here.+
class Egresados(TemplateView):
    template_name = 'Egresados/egresados.html'
 