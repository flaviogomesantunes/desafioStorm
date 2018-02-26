# coding=utf-8
from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import Filme, Genero, Ator


def index(request):
    context = {
        'filmes': Filme.objects.all()
    }
    return render(request, 'catalogo/index.html', context)


def filme(request, slug):
    filme = Filme.objects.filter(slug=slug).first()
    return render(request, 'catalogo/filme.html', filme.as_dict())


def genero(request, slug):
    genero = Genero.objects.filter(slug=slug).first()
    return render(request, 'catalogo/genero.html', genero.as_dict())


def ator(request, slug):
    ator = Ator.objects.filter(slug=slug).first()
    return render(request, 'catalogo/ator.html', ator.as_dict())
