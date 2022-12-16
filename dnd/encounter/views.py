from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm
from monster.models import Monster
from character.models import Character


# Create your views here.
def combat(request):
    if request.method == 'POST':
        # x = request.POST.get('')

        # precesa la info del enemigo y envia todo el statblock de vuelta
        noe = request.POST.get('numenemy')

        enerange = range(1, int(noe))
        enemy = request.POST.get('typenemy')
        monster = Monster.objects.get(moname=enemy)

        # procesa la info de jugadores y envia todos los statblock
        players = Character.objects.all()
        dex = Character.objects.values_list('dex', flat=True)
        nop = len(dex)
        initiative = []
        for times in range(1, nop + 1):
            x = request.POST.get('ini' + str(times))
            y = dex[times-1]
            z = int(x) + y
            initiative.append(z)

        context = {
            'noe': enerange, 
            'enemy': monster, 
            'initiative': initiative, 
            'players': players,
            
            }
        return render(request, "encounter/combat.html", context)
    return render(request, "rte/index.html")
def save():
    s

def index():
    s


