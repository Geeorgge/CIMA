from django.urls import path, include
#from django.contrib.auth.views import LoginView, LogoutView
from GestionAcademicaWebApp import views
from django.contrib.auth.decorators import login_required
from GestionAcademicaWebApp.views import MyLoginView, Registro, Inicio

urlpatterns = [
    
    path('',                 Inicio.as_view(),          name="home"),
    path('aspirantes/',      views.aspirantes,          name='aspirantes'),
    path('contacto/',        views.contacto,            name='contacto'),
    #path('estudiantes/',     views.estudiantes,         name='estudiantes'),
    path('investigadores/',  views.investigadores,      name='investigadores'),
    path('registro/',        Registro.as_view(),        name="registro"),
    path('login/',           MyLoginView.as_view(
                                redirect_authenticated_user=True),      
                                                        name="login"),
    path('logout/',          views.logout,              name="logout"),

    #App egresados urls 
    path('egresados/', include('Egresados.urls')),
    #App Estudiantes urls
    path('estudiantes/', include('Estudiantes.urls')),
    path('admins/',    login_required(views.admins), name="admins"),
      

      
]