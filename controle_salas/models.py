from django.db import models
from datetime import datetime, timedelta
import time
from django.db import connection

# Create your models here.

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade_pessoas = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data = models.DateField(default=datetime.now())
    hora_inicial = models.TimeField(default='00:00:00')
    hora_final = models.TimeField(default='00:00:00')

    class Meta:
        verbose_name_plural = 'Agendamentos'

    def __str__(self):
        return self. sala.nome + ' - ' + str(self.data.strftime('%d-%m-%Y')) + ' | ' \
               + str(self.hora_inicial) + '/' + str(self.hora_final)

    def periodo_disponivel(self, dados):

        hora_inicial = dados['hora_inicial']
        hora_final = dados['hora_final']
        data = dados['data']
        sala = dados['sala']

        query = "SELECT * FROM controle_salas_agenda" \
                " WHERE (hora_inicial <= '" + hora_inicial + "' AND hora_final > '" + hora_inicial + "'" \
                " OR hora_inicial < '" + hora_final + "' AND hora_final >= '" + hora_final + "') " \
                " AND data = '" + data + "' AND sala_id = " + str(sala)

        if 'id' in dados:
            query = query + " AND id <> " + str(dados['id'])

        print(query)

        result = Agenda.objects.raw(query)

        return result
