from rest_framework import serializers
from .models import Filme, Ator, Genero
from django_filters import rest_framework as filters


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['nomeGenero']


class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ator
        fields = ['nomeAtor']


class FilmesSerializer(serializers.ModelSerializer):
    generos = GeneroSerializer(many=True)
    atores = AtorSerializer(many=True)

    class Meta:
        model = Filme
        # fields = '__all__'
        fields = ['nomeFilme', 'resumo']


class FilmeDetalheSerializer(serializers.ModelSerializer):
    generos = GeneroSerializer(many=True)
    atores = AtorSerializer(many=True)

    class Meta:
        model = Filme
        fields = '__all__'


class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ator
        fields = '__all__'
