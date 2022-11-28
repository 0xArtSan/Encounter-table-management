from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Character
from django.forms import ModelForm

class NameForm(forms.Form):
    charname = forms.CharField(label='Character Name', max_length=64)

class NewCharacter(ModelForm):
    class Meta:
        model = Character
        fields = ['charname', 'playername', 'race', 'charclass', 'level', 'ca', 'hp', 'pp', 'str', 'dex', 'con', 'int', 'wis', 'cha'] 


def index(request):
        return render(request, "character/load.html", {
            "characters": Character.objects.all()
        })

def load(request, charname):
    # Arreglar esta funcion para que al darle a buscar te ponga .../load/charname y te cargue su ficha
    charname = charname(request.POST)
    if charname.is_valid():
        character = Character.objects.get(charname=charname)
        # echar un error en caso de que no exista
        return render(request, "character/loaded.hmtl", {
            "character": character
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

