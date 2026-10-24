from django.shortcuts import render
from servicos_app.models import Servico


def servicos(request):
    servicos = Servico.objects.all()

    return render(
        request,
        'servicos/servicos.html',
        {'servicos': servicos}
    )