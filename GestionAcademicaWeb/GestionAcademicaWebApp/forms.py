 
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.forms import Form
from django.forms.models import ModelForm
from django.views.generic.edit import FormView
from GestionAcademicaWebApp.models import CustomUsuarios
 
#from django.contrib.auth.models import Usuarios
#from django.forms import fields, models, ModelForm, widgets
from .models import CustomUsuarios
 
class UserLogin(ModelForm):
    class Meta:
        model = CustomUsuarios
        #La variable "fields", ponemos los campos que tendra este form
        fields = ["email", "password"] 
        widgets = {
            'email'    : forms.EmailInput(      attrs = {'class': 'form-control',    
                                                    'placeholder': 'Correo electrónico...'}),

            'password' : forms.PasswordInput(   attrs = {'class':'form-control',
                                                    'placeholder': 'Contraseña...'}),
            }   

     
         
    def clean(self):
        if self.is_valid():
            email =     self.cleaned_data['email']
            password =  self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Datos incorrectos")


#Formulario para registrar usuarios 
class FormRegistro(UserCreationForm):
    class Meta:
        model = CustomUsuarios
        fields = ['matricula','nombre','apellidos','email','estatus', 'password1','password2']
        widgets = {
            'matricula'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre'     : forms.TextInput(  attrs={'class': 'form-control'}),
            'apellidos'  : forms.TextInput(  attrs={'class': 'form-control'}),
            'email'      : forms.EmailInput( attrs={'class': 'form-control'}),
            'estatus'    : forms.Select(     attrs={'class': 'form-control'}),
             
             }
             
    def __init__(self, *args, **kwargs):
        super(FormRegistro, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control' 
        self.fields['password2'].widget.attrs['class'] = 'form-control' 


    '''def clean(self):
        if self.is_valid():
            matricula    = self.cleaned_data['matricula']
            nombre       = self.cleaned_data['nombre']
            apellidos    = self.cleaned_data['apellidos']
            email        = self.cleaned_data['email']
            estatus      = self.cleaned_data['estatus']
            password1    = self.cleaned_data['password1']
            password2    = self.cleaned_data['password2']
            if not authenticate(matricula = matricula, nombre  = nombre,  apellidos = apellidos,
                                email     = email,     estatus = estatus, password1 = password1,
                                password2 = password2):
                raise forms.ValidationError("Datos incorrectos")'''

    def save(self, commit=True):
        user = super(FormRegistro, self).save(commit=False)
        user.matricula  = self.cleaned_data['matricula']
        user.nombre     = self.cleaned_data['nombre   ']
        user.apellidos  = self.cleaned_data['apellidos']
        user.email      = self.cleaned_data['email    ']
        user.estatus    = self.cleaned_data['estatus  ']
        user.password1  = self.cleaned_data['password1']
        user.password2  = self.cleaned_data['password2']

        if commit:
            user.save()
        return user

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')




 

    