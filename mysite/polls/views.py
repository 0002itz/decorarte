from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    title= "titel_index"
    return render(request,"index.html", {
        'title': title
    })

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")