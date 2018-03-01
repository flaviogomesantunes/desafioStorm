from rest_framework import serializers
from .models import Filme, Ator, Genero
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


class TesteAPISerializer(serializers.ModelSerializer):
    generos = serializers.StringRelatedField(many=True)
    atores = serializers.StringRelatedField(many=True)

    class Meta:
        model = Filme
        fields = '__all__'


class FilmesSerializer(serializers.ModelSerializer):
    generos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Filme
        # fields = '__all__'
        fields = ['nome', 'resumo', 'generos']


class FilmeDetalheSerializer(serializers.ModelSerializer):
    generos = serializers.StringRelatedField(many=True)
    atores = serializers.StringRelatedField(many=True)

    class Meta:
        model = Filme
        fields = '__all__'


class AtorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ator
        fields = '__all__'
