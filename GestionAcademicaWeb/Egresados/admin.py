from django.contrib import admin
from .models import Usuarios, Materias, Cursos
from . import models
#from GestionAcademicaWebApp.models import Usuarios
# Register your models here.

#Registrar modelos
  
admin.site.register(models.Usuarios)
admin.site.register(models.Materias)
admin.site.register(models.Cursos)
 
#Clases para administrar los modelos

#@admin.register(models.Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    #despliega los campos que se muestran en el admin de django
    list_display = ('Matricula', 'Nombre',)
    #Los campos sobre los que se podran hacer busquedas
    search_fields = ('Matricula',)

#@admin.register(models.Materias)
class MateriasAdmin(admin.ModelAdmin):
    list_display = ('nombreCurso', 'tutorCurso',)
    search_fields = ('nombreCurso',)

#@admin.register(models.Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('nombreMateria', 'tutorMateria',)
    search_fields = ('nombreMateria',)
