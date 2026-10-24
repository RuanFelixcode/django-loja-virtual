from django.shortcuts import render
from .models import Produto
# Create your views here.


def loja(request):
    produtos = Produto.objects.all()
    return render(request,'loja/loja.html',{'produtos':produtos})