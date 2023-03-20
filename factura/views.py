from django.http import HttpResponse

def saludo(request): #primera vista
    return HttpResponse("hola esta es mi primera factura electronica")

def despedida(request): 
    return HttpResponse("segunda")