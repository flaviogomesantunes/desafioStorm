# coding=utf-8
"""desafioStorm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
# from django.contrib.auth.models import Filme
from rest_framework import routers

from core import views
from catalogo import views as views_catalogo


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'filmes', views_catalogo.FilmesViewSet, base_name='Filme')
router.register(r'filme_detalhe', views_catalogo.FilmeDetalheViewSet, base_name='FilmeDetalhe')
router.register(r'teste_api', views_catalogo.TesteAPIViewSet, base_name='TesteAPI')
router.register(r'ator', views_catalogo.AtorViewSet, base_name='Ator')

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^$', views_catalogo.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^ator/(?P<slug>[\w_-]+)/$', views_catalogo.ator, name='ator'),
    url(r'^filme/(?P<slug>[\w_-]+)/$', views_catalogo.filme, name='filme'),
    url(r'^genero/(?P<slug>[\w_-]+)/$', views_catalogo.genero, name='genero'),
    url(r'^admin/', admin.site.urls),
]

# serve arquivos estaticos em modo debug
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
