# coding=utf-8
from django.db import models
from django.db.models import Q
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField


class Ator(models.Model):
    nome = models.CharField('Ator', max_length=200)
    slug = AutoSlugField('Identificador', populate_from='nome', unique=True, max_length=200)
    imagem = models.ImageField('Imagem', upload_to='atores', blank=True, null=True)
    pais = models.CharField('País', max_length=100)

    class Meta:
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('ator', kwargs={'slug': self.slug})

    def as_dict(self):
        dict = model_to_dict(self)
        dict['slug'] = self.slug
        dict['filmes'] = [mov.as_simple_dict() for mov in Filme.objects.filter(atores__slug=self.slug)[:20]]
        return dict

    def as_simple_dict(self):
        dict = model_to_dict(self)
        dict['slug'] = self.slug
        return dict


class Genero(models.Model):
    nome = models.CharField('Gênero', max_length=100)
    slug = AutoSlugField('Identificador', populate_from='nome', unique=True, max_length=100)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('genero', kwargs={'slug': self.slug})

    def as_dict(self):
        dict = model_to_dict(self)
        dict['slug'] = self.slug
        dict['filmes'] = [mov.as_simple_dict() for mov in Filme.objects.filter(generos__slug=self.slug)]

    def as_simple_dict(self):
        dict = model_to_dict(self)
        dict['slug'] = self.slug
        return dict


class Filme(models.Model):
    nome = models.CharField('Filme', max_length=200)
    slug = AutoSlugField('Identificador', populate_from='nome', unique=True, max_length=200)
    sinopse = models.TextField('Sinopse', blank=True)
    resumo = models.CharField('Resumo', max_length=150)
    imagem = models.ImageField('Imagem', upload_to='filmes', blank=True, null=True)
    # FK para Atores e Generos do app catalogo
    atores = models.ManyToManyField('catalogo.Ator', verbose_name='Ator')
    generos = models.ManyToManyField('catalogo.Genero', verbose_name='Gênero')
    popularidade = models.IntegerField('Popularidade', default=0)
    trailer = models.CharField('Trailer', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['-popularidade']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('filme', kwargs={'slug': self.slug})

    def as_dict(self):
        # Incrementa o campo popularidade ao retornar os dados de um filme
        self.popularidade = self.popularidade + 1
        self.save()

        # pega os filmes relacionados ao filme que está sendo visualizado
        # através dos atores e generos
        atores = self.atores.all()
        generos = self.generos.all()
        filmes_relacionados = Filme.objects.filter(Q(generos=generos) | Q(atores=atores)).exclude(slug=self.slug).distinct()[:10]
        # filmes_relacionados = Filme.objects.filter((Q(generos=generos), Q(atores=atores)) | (Q(generos=generos) | Q(atores=atores))).exclude(slug=self.slug).distinct()[:10]

        dict = model_to_dict(self)
        dict['slug'] = self.slug
        dict['generos'] = [gen.as_simple_dict() for gen in Genero.objects.filter(filme__slug=self.slug)]
        dict['atores'] = [act.as_simple_dict() for act in Ator.objects.filter(filme__slug=self.slug)]
        dict['filmes'] = [f.as_simple_dict() for f in Filme.objects.filter(atores__slug=self.slug)[:20]]
        dict['filmes_relacionados'] = filmes_relacionados
        return dict

    def as_simple_dict(self):
        dict = model_to_dict(self)
        dict['slug'] = self.slug
        dict.pop('generos', None)
        dict.pop('atores', None)
        dict.pop('filmes', None)
        return dict
