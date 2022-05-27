from django.urls import path

import produtos.views

urlpatterns = [
    path('home/', produtos.views.home, name='home'),
    path('home/adicionar/', produtos.views.adicionar, name='add')
]
