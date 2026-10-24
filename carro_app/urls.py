from django.urls import path
from . import views

app_name = 'carro'

urlpatterns = [path('adicionar_produto/<int:produto_id>/', views.adicionar_produto, name='Adicionar Produto'),
               
path('deletar_produto/<int:produto_id>/', views.deletar_produto, name='Deletar Produto'),

path('diminuir_quantidade/<int:produto_id>/', views.diminuir_quantidade, name='Diminuir Quantidade'),

path('esvaziar_carro/', views.esvaziar_carro, name='Esvaziar Carro'),

]