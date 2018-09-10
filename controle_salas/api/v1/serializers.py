from rest_framework.serializers import ModelSerializer
from controle_salas.models import Sala, Agenda

class SalaSerializer(ModelSerializer):
    class Meta:
        model = Sala
        fields = ('id', 'nome', 'descricao', 'quantidade_pessoas')

class AgendaSerializer(ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'sala', 'data', 'hora_inicial', 'hora_final')