from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, F, FloatField
from loja_app.models import Produto

class Pedido(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.linhapedido_set.aggregate(
            total=Sum(
                F("preco") * F("quantidade"),
                output_field=FloatField()
            )
        )["total"]



class LinhaPedido(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE
    )

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE
    )

    quantidade = models.IntegerField(
        default=1
    )

    preco = models.FloatField(
        default=0
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.quantidade} unidades de {self.produto.nome}"

    class Meta:
        db_table = "linhas_pedido"
        verbose_name = "Linha de Pedido"
        verbose_name_plural = "Linhas de Pedidos"
        ordering = ["id"]
