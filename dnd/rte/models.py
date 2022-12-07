from django.db import models
from django import forms
from django.forms import ModelForm, formset_factory
from monster.models import Monster 

# Create your models here.
class RTE(models.Model):
    tablename = models.CharField(max_length=100, default="nameyourtables")
    tablemons = models.TextField()
