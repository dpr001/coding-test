# Generated by Django 2.1.1 on 2018-09-10 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_salas', '0007_auto_20180909_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='data',
            field=models.DateField(default=datetime.datetime(2018, 9, 10, 18, 28, 42, 785605)),
        ),
    ]
