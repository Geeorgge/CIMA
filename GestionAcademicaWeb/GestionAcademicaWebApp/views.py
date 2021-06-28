from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from GestionAcademicaWebApp.forms import FormRegistro, UserLogin
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as djngo_logout
from django.views.generic import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
 

 #          ****    Vistas basadas en clases    ****

#Despliega la pagina inicial de la web
class Inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'GestionAcademicaWebApp/home.html')

#Despliega la pagina base del modulo de "Aspirantes"
def aspirantes(request):
    return render(request, "GestionAcademicaWebApp/aspirantes.html")

#Despliega la pagina base del modulo de "Investigadores"
def investigadores(request):
    return render(request, "GestionAcademicaWebApp/investigadores.html")


def contacto(request):
    return render(request, "GestionAcademicaWebApp/contacto.html")

#Despliega la pagina base del modulo de "Administrativos"
def admins(request):
    return render(request, "GestionAcademicaWebApp/admins.html")

#Vista basada en clase para el login de la página
class MyLoginView(SuccessMessageMixin, LoginView):
    
    form_class      = UserLogin
    template_name   = 'GestionAcademicaWebApp/login.html'
    success_url     = 'home' 
    success_message = f'Bienvenido a tu cuenta {User}'


    def get_success_url(self) -> str:
        return super().get_success_url()
    
    def get(self, request):
        form = UserLogin()
        return render(request, self.template_name, {'form':form})
     
    def post(self, request): #Funcion que valída los datos insertados: "email", "password"
        contxt = { }
        if request.POST:
            form = UserLogin(request.POST)
            if form.is_valid():
                 
                email     = form.cleaned_data['email']
                password  = form.cleaned_data['password']
                user = authenticate(email=email, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('home')
                else:
                    contxt['LoginForm'] = form
            else:
                form = UserLogin()
                contxt['LoginForm'] = form    

            return render(request, 'GestionAcademicaWebApp/login.html', contxt) 

def logout(request): #Funcion para cerrar sesion
    djngo_logout(request)
    return render(request, "GestionAcademicaWebApp/home.html")
 
#Vista basada en clase para el registro de usuarios
class Registro(FormView): 
    template_name   = 'GestionAcademicaWebApp/registro.html'
    form_class      = FormRegistro
    success_url     = reverse_lazy('GestionAcademicaWebApp/home')
    
     

    def get(self, request, *args, **kwargs):
        form = FormRegistro()
        return render(request,  'GestionAcademicaWebApp/registro.html', {'form':form})

    
    
    def post(self, request ): #Funcion que valída todos los datos insertados
        contxt = {}
        if request.POST:
            form = FormRegistro(request.POST)
            if form.is_valid():
                
                matricula    = form.cleaned_data['matricula']
                nombre       = form.cleaned_data['nombre']
                apellidos    = form.cleaned_data['apellidos']
                email        = form.cleaned_data['email']
                estatus      = form.cleaned_data['estatus']
                
                
                user         = authenticate(matricula = matricula,  nombre  = nombre,
                                            apellidos = apellidos,  email   = email, 
                                            estatus   = estatus)
                user = form.save()                            
                return redirect('login')
            else:               
                contxt['RegistForm'] = form
        else:
            form = FormRegistro()
            contxt['RegistForm'] = form    

        return render(request,  'GestionAcademicaWebApp/registro.html', contxt)

      

 






