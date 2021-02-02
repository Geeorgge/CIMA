from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView 
from django.views.generic.edit import FormView
from .forms import  EncuestaEgresados
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

#from django.forms.models import Usuarios
 


# Create your views here.+
class Egresados(TemplateView):
    template_name = 'Egresados/egresados.html'

 
class Encuesta(FormView):
     
    template_name= 'Egresados/encuesta.html'
    form_class      = EncuestaEgresados
    success_url     = reverse_lazy('home')
    

    def post(self, request, *args, **kwargs):
        contxt = {}
        form =  EncuestaEgresados(request.POST) 
        if form.is_valid():
            opciones    = form.cleaned_data['opciones']
            user        = authenticate(opciones = opciones)
            user = form.save()    
            login(user, backend='GestionAcademicaWebApp.backends.CaseInsensitiveModelBackend' )                       
            print('datos enviados')
            return self.form_valid(form)
        else:
            contxt['EncuestaEgresados'] = form
        
        return render(request,  'Egresados/encuesta.html', contxt)
             


        '''contxt = {}
        if request.POST:
            form = EncuestaEgresados(request.POST)
            if form.is_valid():
                opciones    = form.cleaned_data['opciones']
                user         = authenticate(opciones = opciones)
                user = form.save()                            
                login(self.request, user, backend='GestionAcademicaWebApp.backends.CaseInsensitiveModelBackend' )
                print('datos enviados')
                return redirect('login')
            else:               
                contxt['EncuestaEgresados'] = form
        else:
            form = EncuestaEgresados()
            contxt['EncuestaEgresados'] = form    

        return render(request,  'Egresados/encuesta.html', contxt)'''

    
    
     
    
 