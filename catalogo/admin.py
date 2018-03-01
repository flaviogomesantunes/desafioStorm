# coding=utf-8
from django.contrib import admin
from .models import Ator, Genero, Filme


# personalização do admin
class GeneroAdmin(admin.ModelAdmin):

    list_display = ['nome', 'slug']
    search_fields = ['nome', 'slug']


class AtorAdmin(admin.ModelAdmin):

    list_display = ['nome', 'slug', 'pais']
    search_fields = ['nome', 'slug', 'pais']


class FilmeAdmin(admin.ModelAdmin):

    readonly_fields = ['popularidade']
    list_display = ['nome', 'slug', 'popularidade']
    search_fields = ['nome', 'slug', 'popularidade']


admin.site.register(Ator, AtorAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Filme, FilmeAdmin)
