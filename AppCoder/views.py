from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def crear_curso(request):
    curso = Curso(nombre = 'Python', camada=47785)
    curso.save()
    contexto = {"curso": curso}

    return render(request, 'index.html', contexto)

def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Juan Cruz"}
    return render(request, 'index.html', contexto)