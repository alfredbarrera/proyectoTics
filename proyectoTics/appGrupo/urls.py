from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservas', views.reservas, name='reservas'),
    path('servicios', views.servicios, name='servicios'),
    path('quienes', views.quienes, name='quienes'),
    path('galeria', views.galeria, name='galeria'),
    path('contacto', views.contacto, name='contacto'),
]