from django.urls import path
from . import views
#Para cargar las imagenes en admin
from ProyectoWeb.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('', views.servicios, name='servicios')
]

urlpatterns+=static(MEDIA_URL, document_root=MEDIA_ROOT)