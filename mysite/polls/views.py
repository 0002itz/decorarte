from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#def index(request):
#    title= "titel_index"
#    return render(request,"index.html", {
#        'title': title
#    })
def index(request):
    return render(request, "index.html")

def sigup(request):
    return render(request, "signup.html", {
        'form' : UserCreationForm
    })

def home(request):
    return render(request, "home.html")

def documentos(request):
    return render(request, "documentos.html")

def imagenes(request):
    return render(request, "imagenes.html")

def videos(request):
    return render(request, "videos.html")

def audios(request):
    return render(request, "audios.html")

def calendario(request):
    return render(request, "calendario.html")

