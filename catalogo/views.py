# coding=utf-8
import django_filters.rest_framework
from django.shortcuts import render
# from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from .models import Filme, Genero, Ator
from .serializers import FilmesSerializer, FilmeDetalheSerializer, AtorSerializer
from rest_framework import serializers, viewsets, generics
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import Lower


# Classes das APIs
class FilmesViewSet(viewsets.ModelViewSet):
    serializer_class = FilmesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('generos',)
    
    def get_queryset(self):
        queryset = Filme.objects.all()
        genero = self.request.query_params.get('generos', None)

        if genero is not None:
            queryset = queryset.filter(generos=genero)
        return queryset


class FilmeDetalheViewSet(viewsets.ModelViewSet):
    serializer_class = FilmeDetalheSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nomeFilme', 'slug')

    def get_queryset(self):
        queryset = Filme.objects.all()
        nome_filme = self.request.query_params.get('nomeFilme', None)
        slug_filme = self.request.query_params.get('slug', None)

        if nome_filme is not None:
            queryset = queryset.filter(nomeFilme__iexact=nome_filme)
        elif slug_filme is not None:
            queryset = queryset.filter(slug=slug_filme)
        return queryset


class AtorViewSet(viewsets.ModelViewSet):
    serializer_class = AtorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nomeAtor', 'slug')

    def get_queryset(self):
        queryset = Ator.objects.all()
        nome_ator = self.request.query_params.get('nomeAtor', None)
        slug_ator = self.request.query_params.get('slug', None)

        if nome_ator is not None:
            queryset = queryset.filter(nomeAtor=nome_ator)
        elif slug_ator is not None:
            queryset = queryset.filter(slug=slug_ator)
        return queryset


def index(request):
    order = request.GET.get('ordem')
    page = request.GET.get('page')

    if not page:
        page = 1
    else:
        page = int(page)

    # quantidade de item por pagina
    paginate_by = 10

    if order:
        if order == 'A_Z':
            page_obj = Paginator(Filme.objects.all().order_by('nomeFilme'), paginate_by)
        else:
            page_obj = Paginator(Filme.objects.all().order_by('-nomeFilme'), paginate_by)
    else:
        page_obj = Paginator(Filme.objects.all().order_by('-popularidade'), paginate_by)

    page_atual = page_obj.page(page)
    filmes = page_atual.object_list

    context = {
        'filmes': filmes,
        'ordem': order,
        'page_obj': page_obj,
        'page_atual': page,
    }
    return render(request, 'catalogo/index.html', context)


def filme(request, slug):
    filme = Filme.objects.filter(slug=slug).first()
    return render(request, 'catalogo/filme.html', filme.as_dict())


def genero(request, slug, *args, **kwargs):
    order = request.GET.get('ordem')
    genero_list = Genero.objects.filter(slug=slug)
    page = request.GET.get('page')

    if not page:
        page = 1
    else:
        page = int(page)

    # quantidade de item por pagina
    paginate_by = 10

    if order:
        if order == 'A_Z':
            page_obj = Paginator(Filme.objects.filter(generos=genero_list).order_by('nomeFilme'), paginate_by)
        else:
            page_obj = Paginator(Filme.objects.filter(generos=genero_list).order_by('-nomeFilme'), paginate_by)
    else:
        page_obj = Paginator(Filme.objects.filter(generos=genero_list).order_by('-popularidade'), paginate_by)

    for genero in genero_list:
        header_content = genero.nomeGenero

    page_atual = page_obj.page(page)
    filmes = page_atual.object_list

    context = {
        'header_content': header_content,
        'filmes': filmes,
        'ordem': order,
        'page_obj': page_obj,
        'page_atual': page,
    }
    return render(request, 'catalogo/genero.html', context)


def ator(request, slug):
    ator = Ator.objects.filter(slug=slug).first()
    return render(request, 'catalogo/ator.html', ator.as_dict())
