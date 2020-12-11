from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import View


# Create your views here.


class Inicio(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'GestionAcademicaWebApp/home.html')


def Aspirantes(request):


    return render(request, "GestionAcademicaWebApp/aspirantes.html")





def Investigadores(request):


    return render(request, "GestionAcademicaWebApp/investigadores.html")


def Estudiantes(request):


    return render(request, "GestionAcademicaWebApp/estudiantes.html")


def Contacto(request):


    return render(request, "GestionAcademicaWebApp/contacto.html")

def Admins(request):


    return render(request, "GestionAcademicaWebApp/admins.html")

def Login(request):

    return render(request, "GestionAcademicaWebApp/login.html")

def Logout(request):

    return render(request, "GestionAcademicaWebApp/logout.html")

def Registro(request):

    return render(request, "GestionAcademicaWebApp/registro.html")





