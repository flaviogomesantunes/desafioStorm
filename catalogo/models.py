# coding=utf-8
from django.db import models
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField


class Ator(models.Model):
    nomeAtor = models.CharField('Ator', max_length=200)
    # slug = models.SlugField('Identificador', max_length=100)
    slug = AutoSlugField('Identificador', populate_from='nomeAtor', unique=True, max_length=200)
    imagem = models.ImageField('Imagem', upload_to='atores', blank=True, null=True)
    pais = models.CharField('País', max_length=100)

    class Meta:
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'
        ordering = ['nomeAtor']

    def __str__(self):
        return self.nomeAtor

    def get_absolute_url(self):
        return reverse('ator', kwargs={'slug': self.slug})

    def as_dict(self):
        dictionary = model_to_dict(self)
        dictionary['slug'] = self.slug
        dictionary['filmes'] = [mov.as_simple_dict() for mov in Filme.objects.filter(atores__slug=self.slug)[:20]]
        return dictionary

    def as_simple_dict(self):
        dictionary = model_to_dict(self)
        dictionary['slug'] = self.slug
        return dictionary


class Genero(models.Model):
    nomeGenero = models.CharField('Gênero', max_length=100)
    # slug = models.SlugField('Identificador', max_length=100)
    slug = AutoSlugField('Identificador', populate_from='nomeGenero', unique=True, max_length=100)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['nomeGenero']

    def __str__(self):
        return self.nomeGenero

    def get_absolute_url(self):
        return reverse('genero', kwargs={'slug': self.slug})

    def as_dict(self):
        dictionary = model_to_dict(self)
        dictionary['slug'] = self.slug
        dictionary['filmes'] = [mov.as_simple_dict() for mov in Filme.objects.filter(generos__slug=self.slug)]

    def as_simple_dict(self):
        dictionary = model_to_dict(self)
        dictionary['slug'] = self.slug
        return dictionary


class Filme(models.Model):
    nomeFilme = models.CharField('Filme', max_length=200)
    # slug = models.SlugField('Identificador', max_length=200)
    slug = AutoSlugField('Identificador', populate_from='nomeFilme', unique=True, max_length=200)
    sinopse = models.TextField('Sinopse', blank=True)
    resumo = models.CharField('Resumo', max_length=150)
    imagem = models.ImageField('Imagem', upload_to='filmes', blank=True, null=True)
    # FK para Atores e Generos do app catalogo
    atores = models.ManyToManyField('catalogo.Ator', verbose_name='Ator')
    generos = models.ManyToManyField('catalogo.Genero', verbose_name='Gênero')
    popularidade = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['-popularidade']

    def __str__(self):
        return self.nomeFilme

    def get_absolute_url(self):
        return reverse('filme', kwargs={'slug': self.slug})

    def as_dict(self):
        # Incrementa o campo popularidade ao retornar os dados de um filme
        self.popularidade = self.popularidade + 1
        self.save()

        dictionary = model_to_dict(self)
        dictionary['slug'] = self.slug
        dictionary['generos'] = [gen.as_simple_dict() for gen in Genero.objects.filter(filme__slug=self.slug)]
        dictionary['atores'] = [act.as_simple_dict() for act in Ator.objects.filter(filme__slug=self.slug)]
        return dictionary

    def as_simple_dict(self):
        dictionary = model_to_dict(self)
        dictionary['slug'] = self.slug
        dictionary.pop('generos', None)
        dictionary.pop('atores', None)
        return dictionary
