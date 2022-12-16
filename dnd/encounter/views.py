from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm
from monster.models import Monster
from character.models import Character
import random

# Create your views here.
def combat(request):
    if request.method == 'POST':
        # x = request.POST.get('')

        # precesa la info del enemigo y envia todo el statblock de vuelta
        noe = request.POST.get('numenemy')
        enerange = range(0, int(noe))

        enemies = []
        enemy = request.POST.get('typenemy')
        monster = Monster.objects.filter(moname=enemy).values()
        dex = monster[0]["dex"]
        for enemy in enerange:
            enin = random.randint(1, 20) + dex
            en = monster[0]
            en["ini"] = enin
            enemies.append(en)

        # procesa la info de jugadores y envia todos los statblock
        players = Character.objects.values()
        nop = len(players)
        initiative = []
        for times in range(1, nop + 1):
            x = request.POST.get('ini' + str(times))
            initiative.append(x)
        counter = 0
        for player in players:
            player["ini"] = initiative[counter]
            counter = counter + 1

        context = {
            'noe': enerange, 
            'enemies': enemies, 
            'initiative': initiative, 
            'players': players,
            'prueba': 'pene'
            }
        return render(request, "encounter/combat.html", context)
    return render(request, "rte/index.html")
def save():
    s

def index():
    s


