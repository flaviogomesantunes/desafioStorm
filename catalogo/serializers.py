from rest_framework import serializers
from .models import Filme, Ator, Genero


# class TesteAPISerializer(serializers.ModelSerializer):
#     generos = serializers.StringRelatedField(many=True)
#     atores = serializers.StringRelatedField(many=True)
#
#     class Meta:
#         model = Filme
#         fields = '__all__'
#
#
class FilmesSerializer(serializers.ModelSerializer):
    generos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Filme
        fields = ['nome', 'resumo', 'generos']


class FilmeDetalheSerializer(serializers.ModelSerializer):
    generos = serializers.StringRelatedField(many=True)
    atores = serializers.StringRelatedField(many=True)

    class Meta:
        model = Filme
        fields = '__all__'


class AtorSerializer(serializers.ModelSerializer):
    atores = serializers.StringRelatedField(many=True)

    class Meta:
        model = Filme
        fields = ['atores', 'nome', 'resumo']
