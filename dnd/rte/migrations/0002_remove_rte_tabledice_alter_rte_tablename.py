# Generated by Django 4.1.3 on 2022-12-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rte', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rte',
            name='tabledice',
        ),
        migrations.AlterField(
            model_name='rte',
            name='tablename',
            field=models.CharField(max_length=100),
        ),
    ]
