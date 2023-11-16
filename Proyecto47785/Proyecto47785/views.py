from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def saludo_html(request):
    return  HttpResponse("<b>Hola Django - Coder</b>")

def saludo_nombre(request, nombre):
    return  HttpResponse(f'<h1>Hola {nombre}</h1>')

def saludo_plantilla(request):
    contexto = {
        "nombre": "Juan",
        "edad": 27,
        "pertenencias": [
            {
                "nombre": "PC",
                "uso": 3
            },
            {
                "nombre": "Tele",
                "uso": 5
            }
        ]
    }
    return render(request, "index.html", contexto)