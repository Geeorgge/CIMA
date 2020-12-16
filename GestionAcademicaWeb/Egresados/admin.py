from django.contrib import admin
from . import models
from .models import CustomUsuarios, Materias, Cursos
#from GestionAcademicaWebApp.models import Usuarios
# Register your models here.

#Registrar modelos
  
admin.site.register(models.CustomUsuarios)
admin.site.register(models.Materias)
admin.site.register(models.Cursos)
 
#Clases para administrar los modelos

#@admin.register(models.Usuarios)
class CustomUsuariosAdmin(admin.ModelAdmin):
    #despliega los campos que se muestran en el admin de django
    list_display = ('email', 'username','date_joined', 'is_admin', 'is_staff')
    #Los campos sobre los que se podran hacer busquedas
    search_fields = ('matricula', 'username',)
    readonly_fields = ('id', 'date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

#@admin.register(models.Materias)
class MateriasAdmin(admin.ModelAdmin):
    list_display = ('nombreCurso', 'tutorCurso',)
    search_fields = ('nombreCurso',)

#@admin.register(models.Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('nombreMateria', 'tutorMateria',)
    search_fields = ('nombreMateria',)
