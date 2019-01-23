from rest_framework import serializers
from apps.venda.models import Loja, Auditor, Triangulacao


class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ('cnpj', 'luc', 'razaoSocial')


class AuditorSerializer(serializers.ModelSerializer):
    loja = LojaSerializer(many=True)

    class Meta:
        model = Auditor
        fields = ('nome', 'loja')


class TriangulacaoSerializer(serializers.ModelSerializer):
    loja = LojaSerializer(many=True)

    class Meta:
        model = Triangulacao
        fields = ('vendaInformadaLojista', 'vendaReducaoz', 'vendaAuditoriaPresencial', 'loja')
