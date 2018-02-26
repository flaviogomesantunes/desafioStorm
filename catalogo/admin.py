# coding=utf-8
from django.contrib import admin
from .models import Ator, Genero, Filme


# personalização do admin
class GeneroAdmin(admin.ModelAdmin):

    list_display = ['nomeGenero', 'slug']
    search_fields = ['nomeGenero', 'slug']


class AtorAdmin(admin.ModelAdmin):

    list_display = ['nomeAtor', 'slug']
    search_fields = ['nomeAtor', 'slug']


class FilmeAdmin(admin.ModelAdmin):

    readonly_fields = ['popularidade']
    list_display = ['nomeFilme', 'slug']
    search_fields = ['nomeFilme', 'slug']


admin.site.register(Ator, AtorAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Filme, FilmeAdmin)
