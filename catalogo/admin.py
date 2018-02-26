# coding=utf-8
from django.contrib import admin
from .models import Ator, Genero, Filme


# personalização do admin
class GeneroAdmin(admin.ModelAdmin):

    list_display = ['nomeGenero', 'slug']
    search_fields = ['nomeGenero', 'slug']


class AtorAdmin(admin.ModelAdmin):

    list_display = ['nomeAtor', 'slug', 'pais']
    search_fields = ['nomeAtor', 'slug', 'pais']


class FilmeAdmin(admin.ModelAdmin):

    readonly_fields = ['popularidade']
    list_display = ['nomeFilme', 'slug', 'popularidade']
    search_fields = ['nomeFilme', 'slug', 'popularidade']


admin.site.register(Ator, AtorAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Filme, FilmeAdmin)
