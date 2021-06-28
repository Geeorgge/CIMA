from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView 
from django.views.generic.edit import FormView
from .forms import  EncuestaEgresados
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

 #          ****    Vistas basadas en clases    ****


#Vista basada en clase que muestra la página de "Egresados"
class Egresados(TemplateView):
    template_name = 'Egresados/egresados.html'

#Vista basada en clase que muestra la página de "Encuesta" y despliega la encuesta 
class Encuesta(FormView):
     
    template_name= 'Egresados/encuesta.html'
    form_class      = EncuestaEgresados
    success_url     = reverse_lazy('home')
    

    def post(self, request, *args, **kwargs):
        contxt = {}
        form =  EncuestaEgresados(request.POST) 
        if form.is_valid():
            values  = form.cleaned_data['values']
            user    = authenticate(values = values)                     
            return self.form_valid(form)
        else:
            contxt['EncuestaEgresados'] = form
        
        return render(request,  'Egresados/encuesta.html', contxt)
     

    
    
     
    
 