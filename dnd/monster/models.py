from django.db import models

# Create your models here.
class Monster(models.Model):
        moname = models.CharField(max_length=64, default="Art")
        montype = models.CharField(max_length=25, default="Art")
        cr = models.IntegerField(default=1)
        ca = models.IntegerField(default=10)
        hp = models.IntegerField(default=1)
        drs = models.CharField(max_length=250, default="None")
        speed = models.IntegerField(default=6)
        str = models.IntegerField(default=0)
        dex = models.IntegerField(default=0)
        con = models.IntegerField(default=0)
        int = models.IntegerField(default=0)
        wis = models.IntegerField(default=0)
        cha = models.IntegerField(default=0)
        pp = models.IntegerField(default=10)
        skill_1 = models.CharField(max_length=250, default="ª")
        skill_2 = models.CharField(max_length=250, default="ª")
        skill_3 = models.CharField(max_length=250, default="ª")
        action_1 = models.CharField(max_length=250, default="Attack 1")
        action_2 = models.CharField(max_length=250, default="Attack 2")
        action_3 = models.CharField(max_length=250, default="Attack 3")
        spells = models.TextField(default="Mage Spell list")

        def __str__(self):
            return self.moname
