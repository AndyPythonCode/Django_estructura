from django.contrib import admin
from .models import Servicios

# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):# Que los campos created and updated solo sean leer
    readonly_fields = ('created', 'updated')

#Para añadir en admin
admin.site.register(Servicios, ServiciosAdmin)
