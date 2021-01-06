from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class Estudiantes(TemplateView):
    template_name = 'Estudiantes/estudiantes.html'