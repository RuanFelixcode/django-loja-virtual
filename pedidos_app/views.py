from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carro_app.carro import Carro
from pedidos_app.models import LinhaPedido, Pedido
import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@login_required(login_url='autenticar_usuario/pagina_login')
def processar_pedido(request):

    # Cria o pedido para o usuário logado
    pedido = Pedido.objects.create(
        usuario=request.user
    )

    # Pega o carrinho atual
    carro = Carro(request)

    # Lista para armazenar as linhas do pedido
    linhas_pedido = []

    # Percorre os produtos do carrinho
    for chave, valor in carro.carro.items():

        
        linhas_pedido.append(
    LinhaPedido(
        produto_id=chave,
        quantidade=valor["quantidade"],
        preco=valor["preco"],
        usuario=request.user,
        pedido=pedido
    )
)

    # Salva todas as linhas no banco
    LinhaPedido.objects.bulk_create(linhas_pedido)

    # Envia o e-mail de confirmação
    enviar_email(
    pedido=pedido,
    linhas_pedido=linhas_pedido,
    nome_usuario=request.user.username,
    email_usuario=request.user.email
)

    # Mostra mensagem de sucesso
    messages.success(
        request,
        "O pedido foi criado corretamente!"
    )

    # Volta para a loja
    return redirect('loja')



def enviar_email(pedido, linhas_pedido, nome_usuario, email_usuario):

    assunto = "Pedido realizado com sucesso"

    mensagem = render_to_string(
        "pedidos/email_pedido.html",
        {
            "pedido": pedido,
            "linhas_pedido": linhas_pedido,
            "nome_usuario": nome_usuario,
        }
    )

    mensagem_texto = strip_tags(mensagem)

    email_remetente = os.getenv("EMAIL_HOST_USER")

    send_mail(
        assunto,
        mensagem_texto,
        email_remetente,
        [email_usuario],
        html_message=mensagem
    )
