from django.contrib import admin
from .models import Usuarios, Materias, Cursos

# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Materias)
admin.site.register(Cursos)