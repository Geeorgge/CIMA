from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from GestionAcademicaWebApp import views
from django.contrib.auth.decorators import login_required
from GestionAcademicaWebApp.views import inicio

urlpatterns = [
    
    path('', inicio.as_view(), name="home"),
    path('aspirantes/',views.aspirantes, name='aspirantes'),
    path('contacto/',views.contacto, name='contacto'),
    path('estudiantes/',views.estudiantes, name='estudiantes'),
    #App egresados
    path('egresados/', include('Egresados.urls')),
    path('investigadores/',views.investigadores, name='investigadores'),
    path('admins/',login_required(views.admins), name="admins"),
    #path('login/', views.Login, name ="Login"),
    #path('logout/', views.Logout, name ="Logout"),
    path('registro/', views.registro, name="registro"),
    #path('formeg/', views.FormEg, name="FormEg"),

      
]