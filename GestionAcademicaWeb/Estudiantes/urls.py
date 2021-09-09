"""Egresados app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from GestionAcademicaWebApp import urls
#from django.contrib import admin
from django.urls import path, include
from .views import consultaAcademica, Estudiantes,venue_pdf,reporte_asistencias_estancias,reporte_becas,reporte_datos_generales,reporte_constancia_inscripcion,reporte_puntajes_proceso_inscripcion
from Egresados import views

#from django.contrib.auth.views import views as_views 


urlpatterns = [
    path('',   Estudiantes.as_view(),   name ="estudiantes"),
    path('consultaAcademica',   consultaAcademica.as_view(),   name ="consultaAcademica"),
    path('venue_pdf',venue_pdf,name='venue_pdf'),
    path('reporte_asistencias_estancias',reporte_asistencias_estancias,name='reporte_asistencias_estancias'),
    path('reporte_becas',reporte_becas,name='reporte_becas'),
    path('reporte_datos_generales',reporte_datos_generales,name='reporte_datos_generales'),
    path('reporte_constancia_inscripcion',reporte_constancia_inscripcion,name='reporte_constancia_inscripcion'),
    path('reporte_puntajes_proceso_inscripcion',reporte_puntajes_proceso_inscripcion,name='reporte_puntajes_proceso_inscripcion')
    
]