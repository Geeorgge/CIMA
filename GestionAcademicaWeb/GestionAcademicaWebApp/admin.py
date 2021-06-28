from django.contrib import admin
from . import models
from .models import CustomUsuarios, Materias, Cursos, Encuesta
from django.contrib.auth.admin import UserAdmin
 
#Registrar modelos
  
admin.site.register(models.CustomUsuarios)
admin.site.register(models.Materias)
admin.site.register(models.Cursos)
admin.site.register(models.Encuesta)
 
 
#Clases para administrar los modelos

class CustomUsuariosAdmin(admin.ModelAdmin):
    #despliega los campos que se muestran en el admin de django
    list_display = ('email', 'username','date_joined', 'is_aspirante', 'is_estudiante', 'is_egresado', 'is_investigador', 'is_admintvo', 'is_admin',)
    #Los campos sobre los que se podran hacer busquedas
    search_fields      = ('matricula', 'username',)
    readonly_fields    = ('id', 'date_joined',)
    filter_horizontal  = ()
    list_filter        = ()
    fieldsets          = ()

class MateriasAdmin(admin.ModelAdmin):
    list_display       = ('nombreCurso', 'tutorCurso',)
    search_fields      = ('nombreCurso',)


class CursosAdmin(admin.ModelAdmin):
    list_display       = ('nombreMateria', 'tutorMateria',)
    search_fields      = ('nombreMateria',)


class TextoEncuestaAdmin(admin.ModelAdmin):
    model = Encuesta
    list_display = ('option',)
    list_display = ('asignatura',)
    search_fields = ('users')
