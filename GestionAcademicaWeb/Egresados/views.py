from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render
from Egresados.forms import FormEgresados, UserLogin
from django.views.generic import FormView, CreateView, ListView
#from django.contrib.auth.decorators import login_required
#from django.forms.models import Usuarios
 


# Create your views here.+

 
def Egresados(request):
    form_login = UserLogin()
    FormularioEgresados = FormEgresados()
    if form_login == authenticate and request.method == 'POST':
        form_login = AuthenticationForm(request, data=request.POST)
        return render(request, "Egresados/egresados.html", {'miform':FormularioEgresados})
    else:
        messages.info(request, f'Contraseña o usuario incorrectos')
        return render(request, "Egresados/egresados.html", {'formL':form_login})
         
'''
def Egresados(request):
    return render(request, "Egresados/egresados.html")

def formLog(request):
    form_login = UserLogin()
    return render(request, "Egresados/egresados.html", {'formL':form_login})
    

@login_required
def FormEg(request):
    FormularioEgresados = FormEgresados()
    return render(request,"Templates/egresados.html",{'FormEg':FormularioEgresados})
    '''

def logout_request(request):
    logout(request)
    messages.info(request, "Has salido de tu cuenta")
    return redirect("GestionAcademicaWebApp/egresados.html")


def login_request(request):
    form_login = UserLogin()
    if request.method == "POST":
        #se añaden los datos al form
        form_login = AuthenticationForm(request, data=request.POST)
        #sí el formulario es valido..
        if form_login.is_valid():
            form_login.save(commit=False)
            #se recuperan las credenciales validas introducidad en el login
            usuario = form_login.cleaned_data.get('username')
            contraseña = form_login.cleaned_data.get('password')
            #se verifican las credenciales del usuario          
            user = authenticate(username=usuario, password=contraseña)
            #sí existe un usuario con el mismo nombre y passwrd..
            if user is not None:
                #se hace el login manualmente
                auth.login(request, user)
                #mensaje de logeo
                messages.success(request, f"Estas logeado como {usuario}")
                #se redirecciona al index
                return redirect("GestionAcademicaWebApp/base.html")
            else:
                messages.error(request, "Usuario o contraseña incorrecta")
        else:
            messages.error(request, "Usuario o contraseña incorrecta")

    form_login = AuthenticationForm()
    #se renderiza el form
    return render(request, "Egresados/egresados.html", {"formL": form_login})


'''
def Egresados(request):
    #Se requiere logearse para acceder al formulario de egresados
    #FormularioEgresados = FormEgresados()
    #return render(request, "Egresados/egresados.html", {'miform':FormularioEgresados})
    if UserLogin.is_valid:
       FormularioEgresados = FormEgresados()
       return render(request, "Egresados/egresados.html", {'miform':FormularioEgresados})
    else:
        messages.warning(request, f'Has login primero')
        return render(request, "Egresados/login.html")
    return render(request, "Egresados/egresados.html")
'''
#contraseña del superuser: qwerty_13

'''  
def FormEg(request):
    FormularioEgresados = FormEgresados()
    return render(request,"Templates/egresados.html",{'miform':FormularioEgresados})
           
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
    else:
        form=UserCreationForm()

    context = {'form' : form}
    return render(request, "GestionAcademicaWebApp/registro.html", context)

def get_user(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        #se recuperan las credenciales validas
        usuario = form.cleaned_data.get('username')
        return usuario

 '''