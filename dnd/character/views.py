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


def load(request):
    # Arreglar esta funcion para que al darle a buscar te ponga .../load/"charname" y te cargue su ficha
    # En pos de avanzar, lo voy a hacer en post y no va a salir en la url
    if 'charname' in request.GET:
        charname = request.GET['charname']
        data = Character.objects.filter(charname__icontains=charname)
        # echar un error en caso de que no exista
    else:
        data = Character.objects.all()
    context = {
        'character' : data 
    }
    return render(request, "character/load.html", context)



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

