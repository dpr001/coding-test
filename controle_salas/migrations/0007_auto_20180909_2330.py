# Generated by Django 2.1.1 on 2018-09-09 23:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_salas', '0006_auto_20180909_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='hora_final',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='hora_inicial',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 23, 30, 20, 829750)),
        ),
    ]
