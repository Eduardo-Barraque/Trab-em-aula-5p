from django.db import models
from django.contrib.auth.models import User


class Pedido(models.Model):
    data_criacao = models.CharField(max_length=30)
    valor_total = models.DecimalField(decimal_places=2, max_digits= 8)
    ativo = models.BooleanField()


class PedidoItem(models.Model):
    id_pedido = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Pedido')
    id_prod = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Produto')
    quantidade = models.IntegerField()
    desconto = models.FloatField()


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    quant_estoque = models.IntegerField()
    preco_unit = models.DecimalField(decimal_places=2, max_digits= 8)
    imagem = models.URLField(max_length=300)
    ativo = models.BooleanField()
