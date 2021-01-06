from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuariosManager(BaseUserManager):

    def create_user(self, email, nombre, password=None):
        if not email:
            raise ValueError("Users must have an email addres")
        if not nombre:
            raise ValueError("Users must have a nombre")
        user = self.model(
            email=self.normalize_email(email),
            username=nombre,)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
        #Creando un superusuario
         
    def create_superuser(self, email, nombre, password):
        user = self.create_user(
            email=self.normalize_email(email),
            nombre=nombre,
            password=password,)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'


def get_default_profile_image():
    return "GestionAcademicaWebApp/static/img/pythonimage.png"


class CustomUsuarios(AbstractBaseUser):
    email         = models.EmailField(verbose_name='E-mail',
                                      max_length=50, blank=False, unique=True)
    matricula     = models.IntegerField(verbose_name='Matricula', unique=True, null=True)
    nombre        = models.CharField(max_length=65, unique=True)
    apellidos     = models.CharField(max_length=60, blank=False)
    date_joined   = models.DateTimeField(verbose_name="Date joined", auto_now_add=True)
    is_admin      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to=get_profile_image_filepath,
                                      null=True, blank=True, default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)
    estatus1 = [('1', 'Aspirante'),    ('2', 'Estudiante'), ('3', 'Egresado'), ('4', 'Administrativos'),
                ('5', 'Investigador'), ('6', 'Administrador')]
    estatus     = models.CharField(max_length=20, choices=estatus1, default='Estudiante')

    objects = UsuariosManager()

    # FIELD PARA HACER LOGIN
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['nombre',]

    
    

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def __str__(self):
        return f'Usuario {self.id}: {self.matricula} {self.nombre} {self.apellidos}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Materias(models.Model):
    users          = ManyToManyField(CustomUsuarios)
    nombreMateria  = models.CharField(max_length=50, default='any')
    tutorMateria   = models.CharField(max_length=50, default='any')
    califs         = models.IntegerField(default=70)
    fechaCalifs    = models.DateTimeField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return f'Materias  {self.id}: {self.nombreMateria} {self.tutorMateria}'


class Cursos(models.Model):
    users         = ManyToManyField(CustomUsuarios)
    nombreCurso   = models.CharField(max_length=50, default='any')
    tutorCurso    = models.CharField(max_length=50, default='any')
    fechaCurso    = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f'Cursos  {self.id}: {self.nombreCurso}'
