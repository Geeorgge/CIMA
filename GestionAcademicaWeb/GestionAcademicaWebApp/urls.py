from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from GestionAcademicaWebApp import views
from django.contrib.auth.decorators import login_required
from GestionAcademicaWebApp.views import Inicio

urlpatterns = [
    
    path('', Inicio.as_view(), name="Home"),
    path('aspirantes/',views.Aspirantes, name='Aspirantes'),
    path('contacto/',views.Contacto, name='Contacto'),
    path('estudiantes/',views.Estudiantes, name='Estudiantes'),
    #App egresados
    path('egresados/', include('Egresados.urls')),
    path('investigadores/',views.Investigadores, name='Investigadores'),
    path('admins/',login_required(views.Admins), name="Admins"),
    #path('login/', views.Login, name ="Login"),
    #path('logout/', views.Logout, name ="Logout"),
    path('registro/', views.Registro, name="Registro"),
    #path('formeg/', views.FormEg, name="FormEg"),

      
]