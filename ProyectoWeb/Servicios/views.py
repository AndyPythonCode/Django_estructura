from django.shortcuts import render
from .models import Servicios

# Create your views here.

def servicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'Servicios/servicios.html', {'Servicio':servicios})