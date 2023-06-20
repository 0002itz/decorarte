from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("sigup/", views.sigup, name="sigup"),
    path("home/", views.home, name="home"),
    path("documentos/", views.documentos, name="documentos"),
    path("imagenes/", views.imagenes, name="imagenes"), 
    path("videos/", views.videos, name="videos"),
    path("audios/", views.audios, name="audios"),
    path("calendario/", views.calendario, name="calendario"),
]