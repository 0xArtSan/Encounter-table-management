from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
def save(request):
    return render(request, "character/save.html")

def load(request, name):
    return render(request, "character/load.html", {
        "name": name.capitalize()
    })
