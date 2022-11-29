from django.db import models

# Create your models here.
class Character(models.Model):
        charname = models.CharField(max_length=64, default="Art")
        playername = models.CharField(max_length=64, default="Art")
        race = models.CharField(max_length=25, default="Art")
        charclass = models.CharField(max_length=25, default="Art")
        level = models.IntegerField(default=1)
        ca = models.IntegerField(default=10)
        hp = models.IntegerField(default=1)
        pp = models.IntegerField(default=10)
        str = models.IntegerField(default=0)
        dex = models.IntegerField(default=0)
        con = models.IntegerField(default=0)
        int = models.IntegerField(default=0)
        wis = models.IntegerField(default=0)
        cha = models.IntegerField(default=0)
        
        def __str__(self):
            return self.charname