from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def saludo_html(request):
    return  HttpResponse("<b>Hola Django - Coder</b>")

def saludo_nombre(request, nombre):
    return  HttpResponse(f'<h1>Hola {nombre}</h1>')