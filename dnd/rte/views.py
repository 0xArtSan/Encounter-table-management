from django import forms
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm


# save f(x)
def saverte(request):
    if request.method == "POST":
        return render(request, "rte/tables.html") 

    return render(request, "rte/tables.html") 

# Crear tabla de encuentros
# rte  = random table encounter
# random 1-8 + 1-12 = position in rte
# dropdown de monstruos de la db
# por casilla numero entero o dado o dado + numero entero
# guardar en diccionario de diccionarios?
# tabla1 = {
#   {numero: X o 1d6, moname: 'bicho'}
# }
# no se como guardar la info: quiza en un texto largo y al sacarlo interpretarlo

def loadrte(request):
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
