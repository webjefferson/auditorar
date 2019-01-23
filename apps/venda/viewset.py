from rest_framework import viewsets
from apps.venda.models import Triangulacao, Auditor, Loja
from apps.venda.serializers import AuditorSerializer, LojaSerializer, TriangulacaoSerializer


class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer


class AuditorViewSet(viewsets.ModelViewSet):
    queryset = Auditor.objects.all()
    serializer_class = AuditorSerializer


class TriangulacaoViewSet(viewsets.ModelViewSet):
    queryset = Triangulacao.objects.all()
    serializer_class = TriangulacaoSerializer
