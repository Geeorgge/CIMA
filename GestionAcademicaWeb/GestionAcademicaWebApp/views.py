from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import View


# Create your views here.


class inicio(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'GestionAcademicaWebApp/home.html')


def aspirantes(request):


    return render(request, "GestionAcademicaWebApp/aspirantes.html")





def investigadores(request):


    return render(request, "GestionAcademicaWebApp/investigadores.html")


def estudiantes(request):


    return render(request, "GestionAcademicaWebApp/estudiantes.html")


def contacto(request):


    return render(request, "GestionAcademicaWebApp/contacto.html")

def admins(request):


    return render(request, "GestionAcademicaWebApp/admins.html")

def login(request):

    return render(request, "GestionAcademicaWebApp/login.html")

def logout(request):

    return render(request, "GestionAcademicaWebApp/logout.html")

def registro(request):

    return render(request, "GestionAcademicaWebApp/registro.html")





