from django import forms
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm, formset_factory
from monster.models import Monster
from .models import RTE
import random

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
    # tengo una lista vacia
    finaltables = []
    # saco una lista con las listas de los mostros de la db, las cuales tienen 1 elemento
    tables = RTE.objects.values_list('tablemons')
    # para cada una de esas listas:
    for table in tables:
        # les quito los dos primeros y ultimos caracteres y hago una lista con cada uno de los elementos (por cada "', '")
        xtable = table[0].replace("['", "").replace("']", "").split("', '")
        # la lista creada la añado a la lista que se enviara al html
        finaltables.append(xtable)
    # para cada tabla en la tabla que se enviara
    for list in finaltables:
        # esto deberia sustituir la id del mostro por el nombre del mostro
        listmon(list)
# tratar el texto que sale para que sea tratable por el template
    context = {
        'tables': finaltables
    }
    return render(request, "rte/index.html", context) 
    
# iniciativa 
def prepcomb(request):
    if request.method == "POST":
        table = request.POST.get('table')
        tablemons = RTE.objects.filter(tablename=table).values_list('tablemons')
        # no se por que no me pasa bien la lista de mostros
        listmon(tablemons)

        #calcdicemon = []
        #chomon(calcdicemon, calclist)

        context = {'enemies': tablemons, 'table': table}
        return render(request, "rte/prepcomb.html", context)


def chomon(emptylist, list):
    tabledice = random.randint(1, 10) + random.randint(0, 7)
    item = list[tabledice]
    mon = item.rsplit(None, 1)[-1]
    emptylist.append(mon)

    mondice = item.split(None, 1)[0]
    if 'd' in mondice:
        xdice = mondice.split('d', 1)
        dice = int(xdice[0]) * random.randint(1, int(xdice[1]))
        emptylist.append(dice)
    else:
        emptylist.append(mondice)

def listmon(list):    
    i = 1
    # para cada item de la lista que le han pasado empezando por el segundo item
    for monster in list[1:]:
        # esto saca el ultimom item, es decir la id del mostro
        mondb = monster.rsplit(None, 1)[-1]
        # esto busca el mostro que coincide con dicha id
        monshow = Monster.objects.get(pk=int(mondb))
        # en el caso de encontrar un mostro con esa id
        if Monster.objects.get(pk=int(mondb)):
            # esto convierte el item de la lista en #d## # en #d## moname
            monster = monster.split(None, 1)[0] + ' ' + monshow.moname
            list[i] = monster
        i = i + 1


# calcular que mostro y cuantos y que calcule el iniciativa de mostros y pida iniciativa de jugadores
# quiza con un formulario de pjs activos?

# con el dado puedo hacer una funcion recursiva
# pillas el numero de dados
# def rte(y, x)
#   if 'y' > 1:
#       rte(y-1, x)
#   else:
#       return randomnumber between 1 and x
# algo asi
