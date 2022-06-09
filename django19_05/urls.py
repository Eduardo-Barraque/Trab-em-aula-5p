from django.urls import path

import produtos.views

urlpatterns = [
    path('home/', produtos.views.home, name='home'),
    path('home/adicionar/', produtos.views.adicionar),
    path('home/busca/', produtos.views.busca),
    path('home/lista_produto/', produtos.views.lista_produto),
    path('', produtos.views.redirect_home),
]
