from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from AppCoder.models import Curso
from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Curso
from AppCoder.forms import CursoForm, BusquedaCursoForm
from django.views.generic.detail import DetailView


class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "AppCoder/cursos1.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    success_url = "/app/cursos/listar"
    template_name = "AppCoder/crear_curso.html"
    fields = ["nombre", "camada"]

class CursoActualizacion(UpdateView):
    model = Curso
    success_url = "/app/cursos/listar"
    template_name = "AppCoder/crear_curso.html"
    fields = ["nombre", "camada"]

class CursoEliminar(DeleteView):
    model = Curso
    template_name = 'AppCoder/eliminar_curso.html'
    success_url = '/app/cursos/listar'


def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos,
        "nombre": "Juan Cruz",
        "form": BusquedaCursoForm()
    }
    return render(request, "AppCoder/cursos.html", contexto)

def eliminar_cursos(request):
    nombre = request.GET["nombre"]
    curso = Curso.objects.get(nombre=nombre)
    curso.delete()
    return redirect(request, "AppCoder/cursos.html")



def crear_curso(request):
    curso = Curso(nombre='Python', camada=47785)
    curso.save()

    return redirect("/app/cursos/")

@login_required
def crear_curso_form(request):
    if request.method == "POST":

        curso_formulario = CursoForm(request.POST)
        if curso_formulario.is_valid():
            informacion = curso_formulario.cleaned_data

            curso_crear = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso_crear.save()
            return redirect("/app/cursos/")

    curso_formulario = CursoForm
    contexto = {
        "form": curso_formulario
    }
    return render(request, "AppCoder/crear_curso.html", contexto)

def busqueda_nombre(request):
    nombre = request.GET["nombre"]
    cursos = Curso.objects.filter(nombre__icontains=nombre)

    contexto = {
        "cursos": cursos,
        "nombre": "Juan",
        "form": BusquedaCursoForm()
    }

    return render(request, "AppCoder/cursos.html", contexto)

def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Juan Cruz"}
    return render(request, 'index.html', contexto)
