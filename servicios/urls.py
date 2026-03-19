
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.servicios_view, name='servicios'),
    path('servicios/crear/',views.crear_servicios, name='crear_servicios'),
    
]




