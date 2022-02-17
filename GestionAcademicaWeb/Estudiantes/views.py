from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from django.http import FileResponse
import io
from reportlab import cmp
from reportlab.lib import colors, pagesizes
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus.tables import Table, TableStyle

 
# Create your views here.
class Estudiantes(TemplateView):
    template_name = 'Estudiantes/estudiantes.html'
    
class consultaAcademica(TemplateView):
    template_name = 'Estudiantes/consultaAcademica.html'
    
    
#//////////////////////REPORTES///////////////////


#/////////////////////FUNCION PARA IMPRIMIR ///////////////////
def venue_pdf(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter, bottomup=0) #SE DA FORMATO DE HOJA (TIPO CARTA, ETC)
    # textob=c.beginText()
    # textob.setTextOrigin(inch,inch)
    # textob.setFont("Helvetica",14)
    
    # lines=["This is line 1",
    #        "This is line 2",
    #        "This is line 3"]
    
    # for line in lines:
    #     textob.textLine(line)
    
    #////////FORMATO DE LETRA A TITULOS/////////////
    c.setFont("Helvetica",35)
    c.drawCentredString(280,50,"Kardex")
    c.setFont("Helvetica",16)
    c.drawCentredString(300,150,"Nombre del alumno: ")
    
    #//////SE DEFINEN LOS ENCABEZADOS DE LAS COLUMNAS
    encabezados=('IdMateria','Nombre','Ordinario','Extraordinario')
    detalles=[['123456','matematicas','90','0'],['123456','quimica','80','0'],['123456','programacion 1','90','0']] #REEMPLAZAR ESTOS DATOS POR DATOS DEL MODELO DEL ESTUDIANTE
    detalle_orden=Table([encabezados]+detalles,colWidths=[150,100,100]) # //// FORMATO A LAS COLUMNAS DEL REPORTE
    detalle_orden.setStyle(TableStyle([
        ('ALIGN',(0,0),(0,0),'CENTER'),
        ('GRID',(0,0),(-1,-1),1,colors.black),
        ('FONTSIZE',(0,0),(-1,-1),9),
    ]))
    
    detalle_orden.wrapOn(c,500,350)
    detalle_orden.drawOn(c,70,200)
    
    #FORMATO A DATOS PERSONALES, FALTA AGREGAR ESE DATO DIRECTAMENTE DEL MODELO DEL ALUMNO
    c.setFont("Helvetica",18)
    c.drawCentredString(300,650,"Nombre facultad o escuela: ")
    
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf,as_attachment=True,filename='reporteKardex.pdf') #////////SE IMPRIME EL REPORTE AL LLAMAR A LA VISTA
    
def reporte_asistencias_estancias(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter, bottomup=0)
    
    #////////FORMATO DE LETRA A TITULOS/////////////
    c.setFont("Helvetica",20)
    c.drawCentredString(300,60,"Registro de Asistencias a Estancias de Investigación")
    c.setFont("Helvetica",16)
    c.drawCentredString(300,150,"Nombre del alumno: ")
    
    
    #FORMATO A DATOS PERSONALES, FALTA AGREGAR ESE DATO DIRECTAMENTE DEL MODELO DEL ALUMNO
    c.setFont("Helvetica",18)
    c.drawCentredString(300,650,"Nombre facultad o escuela: ")
    
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf,as_attachment=True,filename='reporteAsistenciasEstancias.pdf')#////////SE IMPRIME EL REPORTE AL LLAMAR A LA VISTA
    
def reporte_becas(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter, bottomup=0)
    
    #////////FORMATO DE LETRA A TITULOS/////////////
    c.setFont("Helvetica",20)
    c.drawCentredString(300,60,"Historial de Registro de Becas")
    c.setFont("Helvetica",16)
    c.drawCentredString(300,150,"Nombre del alumno: ")
    
    
    
    c.setFont("Helvetica",18)
    c.drawCentredString(300,650,"Nombre facultad o escuela: ")
    
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf,as_attachment=True,filename='reporteBecas.pdf')#////////SE IMPRIME EL REPORTE AL LLAMAR A LA VISTA

def reporte_datos_generales(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter, bottomup=0)
    
    #////////FORMATO DE LETRA A TITULOS/////////////
    c.setFont("Helvetica",20)
    c.drawCentredString(300,60,"Datos Generales del Alumno")
    c.setFont("Helvetica",16)
    c.drawCentredString(300,150,"Nombre del alumno: ")
    
    c.setFont("Helvetica",16)
    c.drawCentredString(100,250,"Semestre: ")
    
    c.setFont("Helvetica",16)
    c.drawCentredString(100,300,"Dirección: ")
    
    c.setFont("Helvetica",16)
    c.drawCentredString(100,350,"Telefono/Celular: ")
    
    c.setFont("Helvetica",18)
    c.drawCentredString(300,650,"Nombre facultad o escuela: ")
    
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf,as_attachment=True,filename='reporteDatosGenerales.pdf')#////////SE IMPRIME EL REPORTE AL LLAMAR A LA VISTA

def reporte_constancia_inscripcion(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter, bottomup=0)
    
    c.setFont("Helvetica",20)
    c.drawCentredString(300,60,"Constancia de Inscripción")
    c.setFont("Helvetica",16)
    c.drawCentredString(300,150,"Nombre del alumno: ")
    
    
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf,as_attachment=True,filename='reporteConstanciaInscripcion.pdf')#////////SE IMPRIME EL REPORTE AL LLAMAR A LA VISTA

def reporte_puntajes_proceso_inscripcion(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter, bottomup=0)
    
    #////////FORMATO DE LETRA A TITULOS/////////////
    c.setFont("Helvetica",20)
    c.drawCentredString(300,60,"Reporte de Puntajes de Proceso de Inscripción")
    c.setFont("Helvetica",16)
    c.drawCentredString(300,150,"Nombre del alumno: ")
    
    
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf,as_attachment=True,filename='reportePuntajesInscripcion.pdf')#////////SE IMPRIME EL REPORTE AL LLAMAR A LA VISTA