from django.shortcuts import render
# Create your views here.
from carro_app.carro import Carro

def home(request):
    carro = Carro
    return render(request,'projeto_web_app/home.html' )


