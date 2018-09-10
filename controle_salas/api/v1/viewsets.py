from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from controle_salas.models import Sala, Agenda
from .serializers import SalaSerializer, AgendaSerializer

class SalaViewSet(ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class AgendaViewSet(ModelViewSet):

    serializer_class = AgendaSerializer

    def get_queryset(self):
        data_param = self.request.query_params.get('data', None)
        sala_param = self.request.query_params.get('sala', None)

        queryset = Agenda.objects.all()

        if data_param:
            queryset = queryset.filter(data=data_param)

        if sala_param:
            print(sala_param)
            queryset = queryset.filter(sala=sala_param)

        return queryset

    def create(self, request, *args, **kwargs):

        if(Agenda.periodo_disponivel(Agenda, request.data)):
            return Response({'Erro':'Período não disponível'}, status=400)

        return super(AgendaViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):

        if Agenda.periodo_disponivel(Agenda, request.data):
            return Response({'Erro':'Período não disponível'}, status=400)

        return super(AgendaViewSet, self).update(request, *args, **kwargs)