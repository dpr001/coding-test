# Generated by Django 2.1.1 on 2018-09-09 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_salas', '0005_agenda'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agenda',
            options={'verbose_name_plural': 'Agendamentos'},
        ),
        migrations.AddField(
            model_name='agenda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 23, 26, 12, 272927)),
        ),
    ]