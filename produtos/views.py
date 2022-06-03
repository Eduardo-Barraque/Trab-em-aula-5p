import form as form
from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from .models import Produto,Pedido,PedidoItem

# Create your views here.


def home(request):
    lista_produto = Produto.objects.all()
    return render(request, "index.html", {'lista_produto': lista_produto})

def adicionar(request):
    if request.method == "POST":
        produto = Produto()
        produto.nome = request.POST.get('nome', None)
        produto.quant_estoque = int(request.POST.get('quant_estoque', None))
        produto.preco_unit = request.POST.get('preco_unit', None)
        produto.imagem = request.POST.get('imagem', None)
        produto.ativo = True
        produto.save()
        return HttpResponseRedirect('/home/')
