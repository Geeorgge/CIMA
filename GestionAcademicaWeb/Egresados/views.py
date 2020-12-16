 
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render
from django.views.generic.edit import FormView
from Egresados.forms import FormEgresados, UserLogin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
#from django.contrib.auth.decorators import login_required
#from django.forms.models import Usuarios
 


# Create your views here.+

class MyLoginView(SuccessMessageMixin ,LoginView):
    form_class = UserLogin
    template_name = 'Egresados/login.html'
    success_url = "Egresados/egresados.html"
    success_message = f'Welcome to your profile {User}'

    def form_invalid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_valid(form)

def egresados(request):
    form_login = UserLogin()
     
    return render(request, "Egresados/proofs.html", {'formlogin': form_login})
   
class MyFormEgresados(SuccessMessageMixin, FormView):
    form_class = FormEgresados
    template_name = 'formeg.html'
    success_message = 'User registred'
    success_url = "Egresados/egresados.html"

    def form_invalid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_valid(form)

def proofs(request):
    form_egresados = FormEgresados()
    return render(request,"Egresados/egresados.html",{'formegresados':form_egresados}) 



def FormEg(request):
    form_egresados = FormEgresados()
    return render(request,"Egresados/egresados.html",{'formegresados':form_egresados})

'''
def egresados(request):
    form_login = UserLogin()
    FormularioEgresados = FormEgresados()
    if User == authenticate and request.method == 'POST':
        #messages.info(request, f"estas loqueado como {User}")
        form_login = AuthenticationForm(request, data=request.POST)
        return render(request, "Egresados/egresados.html", {'miform':FormularioEgresados})
    else:
        #messages.info(request, f'Contraseña o usuario incorrectos wey')
        return render(request, "Egresados/egresados.html", {'formL':form_login})




def egresados(request):
    #form_login = UserLogin()
    #FormularioEgresados = FormEgresados()
    return render(request, "Egresados/egresados.html" )'''

'''def formLog(request):
    form_login = UserLogin()
    return render(request, "Egresados/egresados.html", {'formL':form_login})
    

#@login_required
def FormEg(request):
    FormularioEgresados = FormEgresados()
    return render(request,"Egresados/egresados.html",{'FormEg':FormularioEgresados})
   



def login_request(request):
    form = UserLogin()
    if request.method == "POST":
        #se añaden los datos al form
        form = AuthenticationForm(request, data=request.POST)
        #sí el formulario es valido..
        if form.is_valid():
            #form.save()
            #se recuperan las credenciales validas introducidad en el login
            usuario = form.cleaned_data['usuario']
            contraseña = form.cleaned_data['contraseña']
            
            #se verifican las credenciales del usuario          
            user = authenticate( username=usuario, password=contraseña)
            #sí existe un usuario con el mismo nombre y passwrd..
            if user is not None:
                #se hace el login manualmente
                auth.login(request, user)
                #mensaje de logeo
                messages.success(request, f"Estas logeado como {user}")
                #se redirecciona al inicio
                return redirect("GestionAcademicaWebApp/base.html")
            else:
                messages.error(request, "Usuario o contraseña incorrectasasasas")
        else:
            messages.error(request, "Usuario o contraseña incorrectauwuwuwu")

    form = AuthenticationForm()
    #se renderiza el form
    return render(request, "Egresados/egresados.html", {"formL": form})
    '''





def logout_request(request):
    logout(request)
    messages.info(request, "Has salido de tu cuenta papu")
    return redirect("Egresados/logout.html")

  