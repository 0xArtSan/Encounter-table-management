from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

class NewCharacter(forms.Form):
        charname = forms.CharField(label="Character Name")
        # playername = forms.CharField(label="Player Name")
        # race = forms.CharField(label="Race")
        # charclass = forms.CharField(label="Class")
        # level = forms.IntegerField(label="Level", max_value=20)
        # ca = forms.IntegerField(label="Class Armor")
        # hp = forms.IntegerField(label="Hit Points")
        # pp = forms.IntegerField(label="Passive Perception")
        # str = forms.IntegerField(label="Strenght", max_value=22)
        # dex = forms.IntegerField(label="Dexterity", max_value=22)
        # con = forms.IntegerField(label="Constitution", max_value=22)
        # int = forms.IntegerField(label="Intelligence", max_value=22)
        # wis = forms.IntegerField(label="Wisdom", max_value=22)
        # cha = forms.IntegerField(label="Charisma", max_value=22)

def load(request):
    if "characters" not in request.session:
        request.session["characters"] = []

    return render(request, "character/load.html", {
        "characters": request.session["characters"]
    })

def save(request):
    if request.method == "POST":
        form = NewCharacter(request.POST)
        if form.is_valid():
            character = form.cleaned_data["charname"]
            request.session["characters"] += [character]
            #aqui hay que meterlo en la base de datos
            return HttpResponseRedirect(reverse("character:load"))

        else:
            return render(request, "character/save.html", {
                "form": form
            })

    return render(request, "character/save.html", {
        "form": NewCharacter()
    })

