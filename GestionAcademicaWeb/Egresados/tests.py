from django.test import TestCase 
from django.core.wsgi import *
from Egresados.models import *
#import sys
#sys.path.append('GestionAcademicaWeb/')
# Create your tests here.

cueri = Usuarios.objects.all()
print(cueri)