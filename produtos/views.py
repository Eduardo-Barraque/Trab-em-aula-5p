import form as form
from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from .models import Produto, Pedido, PedidoItem

# Create your views here.


def redirect_home(request):
    return HttpResponseRedirect('/home/')


def home(request):
    return render(request, "index.html")


def lista_produto(request):
    lista_produto = Produto.objects.all()
    return render(request, "produto.html", {'lista_produto': lista_produto})


def adicionar(request):
    if request.method == "POST":
        produto = Produto()
        produto.nome = request.POST.get('nome', None)
        produto.quant_estoque = request.POST.get('quant_estoque', None)
        produto.preco_unit = request.POST.get('preco_unit', None)
        produto.imagem = request.POST.get('imagem', None)
        produto.ativo = True
        produto.save()
        return HttpResponseRedirect('/home/')


def busca(request):
    search = request.GET.get('palavra_chave')
    if search == '':
        return HttpResponseRedirect('/home/')

    else:
        resultado_busca = Produto.objects.filter(nome__icontains=search)
        amazon = []
        return render(request, "produto.html", {'lista_produto': resultado_busca})

