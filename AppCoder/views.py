from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Curso

def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos,
        "nombre": "Juan Cruz"
    }
    return render(request, "AppCoder/cursos.html", contexto)

def crear_curso(request):
    curso = Curso(nombre = 'Python', camada=47785)
    curso.save()

    return redirect("/app/cursos/")

def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Juan Cruz"}
    return render(request, 'index.html', contexto)