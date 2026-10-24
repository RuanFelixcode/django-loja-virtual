from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import FormularioContato


def contato(request):
    formulario_contato = FormularioContato()

    if request.method == 'POST':
        formulario_contato = FormularioContato(data=request.POST)

        if formulario_contato.is_valid():
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            conteudo = request.POST.get('conteudo')

            mensagem_email = EmailMessage(
                'Mensagem enviada pelo formulário do site',

                'O usuário com nome {} e com o endereço de e-mail {} '
                'escreveu o seguinte:\n\n{}'.format(
                    nome,
                    email,
                    conteudo
                ),

                '',
                ['ruan.felix6@aluno.senai.br'],

                reply_to=[email]
            )

            try:
                mensagem_email.send()
                return redirect('/contato/?valido=1')

            except:
                return redirect('/contato/?novalido=1')

    return render(
        request,
        'contato/contato.html',
        {'meu_formulario': formulario_contato}
    )