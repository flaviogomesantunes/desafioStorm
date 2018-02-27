# coding=utf-8
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from .models import Filme, Genero, Ator


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
