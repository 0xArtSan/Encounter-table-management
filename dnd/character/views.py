from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Character
from django.forms import ModelForm

class NewCharacter(ModelForm):
    class Meta:
        model = Character
        fields = ['charname', 'playername', 'race', 'charclass', 'level', 'ca', 'hp', 'pp', 'str', 'dex', 'con', 'int', 'wis', 'cha'] 


def load(request):
    if request.method == "POST":
        s
    
    else:
        return render(request, "character/load.html", {
            "characters": Character.objects.all()
        })

def save(request):
    if request.method == "POST":
        form = NewCharacter(request.POST)
        if form.is_valid():
            form.save()
            #aqui hay que meterlo en la base de datos
            return HttpResponseRedirect(reverse("character:load"))

        else:
            return render(request, "character/save.html", {
                "form": form
            })

    return render(request, "character/save.html", {
        "form": NewCharacter()
    })

