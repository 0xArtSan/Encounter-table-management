from django.db import models

# Create your models here.
class Monster(models.Model):
        moname = models.CharField(max_length=64, default="Monster")
        montype = models.CharField(max_length=25, default="Medium Humanoid")
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
        skill_1 = models.CharField(max_length=250, default="None")
        skill_2 = models.CharField(max_length=250, default="None")
        skill_3 = models.CharField(max_length=250, default="None")
        action_1 = models.CharField(max_length=250, default="None")
        action_2 = models.CharField(max_length=250, default="None")
        action_3 = models.CharField(max_length=250, default="None")
        spells = models.TextField(default="None")

        def __str__(self):
            return self.moname
