# Generated by Django 4.1.3 on 2022-12-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RTE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tablename', models.CharField(default='nameyourtables', max_length=100)),
                ('tabledice', models.CharField(default='1d8+1d12', max_length=100)),
                ('tablemons', models.TextField()),
            ],
        ),
    ]
