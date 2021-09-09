# Generated by Django 3.1.1 on 2020-12-15 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCurso', models.CharField(default='any', max_length=50)),
                ('tutorCurso', models.CharField(default='any', max_length=50)),
                ('fechaCurso', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMateria', models.CharField(default='any', max_length=50)),
                ('tutorMateria', models.CharField(default='any', max_length=50)),
                ('califs', models.IntegerField(default=70)),
                ('fechaCalifs', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matricula', models.CharField(default='any', max_length=10)),
                ('Nombre', models.CharField(default='any', max_length=40)),
                ('Apellidos', models.CharField(default='any', max_length=65)),
                ('Email', models.CharField(default='any', max_length=50)),
                ('estatus', models.CharField(choices=[('1', 'Aspirante'), ('2', 'Estudiante'), ('3', 'Egresado'), ('4', 'Administrativos'), ('5', 'Investigador'), ('6', 'Administrador')], default='Aspirante', max_length=20)),
                ('cursos', models.ManyToManyField(to='GestionAcademicaWebApp.Cursos')),
                ('materias', models.ManyToManyField(to='GestionAcademicaWebApp.Materias')),
            ],
        ),
    ]