# coding=utf-8
from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import Filme, Genero, Ator


def index(request):
    order = request.GET.get('ordem')

    if order:
        if order == 'A_Z':
            filmes = Filme.objects.all().order_by('nomeFilme')
        else:
            filmes = Filme.objects.all().order_by('-nomeFilme')
    else:
        filmes = Filme.objects.all().order_by('-popularidade')

    context = {
        'filmes': filmes,
        'ordem': order,
    }
    return render(request, 'catalogo/index.html', context)


def filme(request, slug):
    filme = Filme.objects.filter(slug=slug).first()
    return render(request, 'catalogo/filme.html', filme.as_dict())


def genero(request, slug, *args, **kwargs):
    order = request.GET.get('ordem')
    genero_list = Genero.objects.filter(slug=slug)

    if order:
        if order == 'A_Z':
            filmes = Filme.objects.filter(generos=genero_list).order_by('nomeFilme')
        else:
            filmes = Filme.objects.filter(generos=genero_list).order_by('-nomeFilme')
    else:
        filmes = Filme.objects.filter(generos=genero_list).order_by('-popularidade')

    for genero in genero_list:
        header_content = genero.nomeGenero

    context = {
        'header_content': header_content,
        'filmes': filmes,
        'ordem': order,
    }
    return render(request, 'catalogo/genero.html', context)


def ator(request, slug):
    ator = Ator.objects.filter(slug=slug).first()
    return render(request, 'catalogo/ator.html', ator.as_dict())
