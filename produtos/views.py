import form as form
from django.http import request
from django.shortcuts import render
from .models import Produto,Pedido,PedidoItem

# Create your views here.


def home(request):
    lista_produto = Produto.objects.all()
    return render(request, "index.html", {'lista_produto': lista_produto})

def add_page():
    return render(request)

def adicionar(post):
    Produto.nome = request.form.get('product_nome', None)

    Produto.save()
