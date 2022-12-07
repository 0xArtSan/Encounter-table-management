from django import forms
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm, formset_factory
from monster.models import Monster
from .models import RTE

DICE_CHOICE = ['None', 'd4', 'd6', 'd8', 'd10', 'd12']
# create table f(x)
def table(request):
    rows = range(1,18)
    monsterlist = Monster.objects.all()
    if request.method == "POST":
        tablename = request.POST.get('tablename')
        if not tablename:
            failure = 'Provide a tablename'
            context = {'range': rows, 'monsters': monsterlist, 'dices': DICE_CHOICE, 'failure': failure}
            return render(request, "rte/table.html", context)
            
        if RTE.objects.filter(tablename=tablename).exists():
            failure = 'Tablename already in use'
            context = {'range': rows, 'monsters': monsterlist, 'dices': DICE_CHOICE, 'failure': failure}
            return render(request, "rte/table.html", context)

        fintab = [tablename]
        for info in rows:
            numd = 'nod' + str(info)
            typed = 'dice' + str(info)
            monsd = 'monster' + str(info)
            nod = request.POST.get(numd)
            dice = request.POST.get(typed)
            monster = request.POST.get(monsd)
            if dice == 'None':
                apinfo = nod + ' ' + monster
            else:
                apinfo = nod + dice + ' ' + monster

            fintab.append(apinfo)
        
        rte = RTE(tablename=fintab[0], tablemons=fintab)
        rte.save()
        return HttpResponseRedirect(reverse("rte:loadrte"))

    context = {
        'range': rows,
        'monsters': monsterlist,
        'dices': DICE_CHOICE
    }
    return render(request, "rte/table.html", context)

# save table f(x)

def loadrte(request):
    tables = RTE.objects.all()
    context = {
        'tables': tables
    }
    return render(request, "rte/index.html") 
    
# usar la tabla f(x) 

# seleccionar tabla y que calcule el dado
#
# con el dado puedo hacer una funcion recursiva
# pillas el numero de dados
# def rte(y, x)
#   if 'y' > 1:
#       rte(y-1, x)
#   else:
#       return randomnumber between 1 and x
# algo asi
# 
# con el resultado sacame el monstruo/monstruos y llevalos a encounter
