# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-03-01 15:53
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_filme_trailer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ator',
            options={'ordering': ['nome'], 'verbose_name': 'Ator', 'verbose_name_plural': 'Atores'},
        ),
        migrations.AlterModelOptions(
            name='genero',
            options={'ordering': ['nome'], 'verbose_name': 'Gênero', 'verbose_name_plural': 'Gêneros'},
        ),
        migrations.RenameField(
            model_name='ator',
            old_name='nomeAtor',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='filme',
            old_name='nomeFilme',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='genero',
            old_name='nomeGenero',
            new_name='nome',
        ),
        migrations.AlterField(
            model_name='ator',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=200, populate_from='nome', unique=True, verbose_name='Identificador'),
        ),
        migrations.AlterField(
            model_name='filme',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=200, populate_from='nome', unique=True, verbose_name='Identificador'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from='nome', unique=True, verbose_name='Identificador'),
        ),
    ]
