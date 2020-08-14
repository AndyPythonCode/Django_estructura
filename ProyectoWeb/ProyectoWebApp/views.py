from django.shortcuts import render
from Servicios.models import Servicios #Importar la class servicios para los objects

# Create your views here.

def contacto(request):
    return render(request, 'ProyectoWebApp/contacto.html')

def home(request):
    return render(request, 'ProyectoWebApp/home.html')

def blog(request):
    return render(request, 'ProyectoWebApp/blog.html')

def tienda(request):
    return render(request, 'ProyectoWebApp/tienda.html')


