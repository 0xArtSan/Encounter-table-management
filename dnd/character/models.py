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
        str = models.IntegerField(default=8)
        dex = models.IntegerField(default=8)
        con = models.IntegerField(default=8)
        int = models.IntegerField(default=8)
        wis = models.IntegerField(default=8)
        cha = models.IntegerField(default=8)
        
        def __str__(self):
            return f"{self.charname} ({self.playername}) {self.race} {self.charclass} ({self.level}) -- CA:{self.ca}, HP:{self.hp}, PP:{self.pp} -- Str:{self.str} Dex:{self.dex} Con:{self.con} Int:{self.int} Wis:{self.wis} Cha:{self.cha}"