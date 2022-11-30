from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Monster
from django.forms import ModelForm

class NewMon(ModelForm):
    class Meta:
        model = Monster
        fields =['moname', 'montype', 'cr', 'ca', 'hp', 'drs', 'speed', 'str', 'dex', 'con', 'int', 'wis', 'cha', 'pp', 'skill_1', 'skill_2', 'skill_3', 'action_1', 'action_2', 'action_3', 'spells']

def load(request):
    if 'moname' in request.GET:
        moname = request.GET['moname']
        data = Monster.objects.filter(moname__icontains=moname)
    else:
        data = Monster.objects.all()
    context = {
        'monsters' : data
    }
    return render(request, "monster/load.html", context)

def save(request):
    if request.method == "POST":
        form = NewMon(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("monster:loadmon"))
        
        else:
            return render(request, "monster/save.html", {
                "form" : form
            })

    return render(request, "monster/save.html", {
        "form": NewMon()
    })