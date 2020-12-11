from django.contrib.auth import authenticate
from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.



class Materias(models.Model):
  nombreMateria = models.CharField(max_length=50, default='any')
  tutorMateria = models.CharField(max_length=50, default='any')
  califs = models.IntegerField(default=70)
  fechaCalifs = models.DateTimeField (auto_now=False, null = True, blank=True)

  def __str__(self):
        return self.nombreMateria

class Cursos(models.Model):
  nombreCurso = models.CharField(max_length=50, default='any')
  tutorCurso = models.CharField(max_length=50, default='any')
  fechaCurso = models.DateTimeField (auto_now=True, null = True, blank=True)
  
  def __str__(self):
        return self.nombreCurso


class Usuarios(models.Model):
  Matricula = models.CharField(max_length=10,blank=False, null=False, default='any')
  Nombre = models.CharField( max_length=40, blank=False, null=False, default='any')
  Apellidos = models.CharField(max_length=65, blank=False, null=False, default='any')
  Email = models.CharField(max_length=50,blank=False, null=False, default='any')
  #Password = models.CharField(max_length=30,blank=False, null=False, default='any')
  estatus1 = [('1', 'Aspirante') , ('2', 'Estudiante'), ('3', 'Egresado'), 	('4', 'Administrativos'), 
  ('5', 'Investigador'), ('6', 'Administrador')]
  estatus = models.CharField(max_length=20, choices=estatus1, default='Aspirante')
  materias = ManyToManyField(Materias)
  cursos = ManyToManyField(Cursos)
   
  def __str__(self):
        return self.Nombre
  
  
 # def users(request):
  #  usuario = authenticate()
    


    
 

