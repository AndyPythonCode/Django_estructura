from django.urls import path 
from . import views

urlpatterns = [
    #Todas los url de esta app
    path('',views.home, name='home'),
    path('blog/',views.blog, name='blog'),
    path('tienda/',views.tienda, name='tienda'),
    path('contacto/',views.contacto, name='contacto'),
]


