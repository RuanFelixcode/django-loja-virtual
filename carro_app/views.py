from .carro import Carro
from django.shortcuts import redirect
from loja_app.models import Produto


def adicionar_produto(request, produto_id):

    carro = Carro(request)
    produto = Produto.objects.get(id=produto_id)
    carro.adicionar(produto)
    
    return redirect('loja')

def deletar_produto(request,produto_id):
    carro = Carro(request)
    produto = Produto.objects.get(id=produto_id)
    carro.eliminar(produto)

    return redirect('loja')

def diminuir_quantidade(request,produto_id):
    carro = Carro(request)
    produto = Produto.objects.get(id=produto_id)
    carro.diminuir(produto)

    return redirect('loja')

def esvaziar_carro(request):
    carro = Carro(request)
    carro.limpar_carro()

    return redirect('loja')







