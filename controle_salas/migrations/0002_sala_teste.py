# Generated by Django 2.1.1 on 2018-09-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_salas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='teste',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]