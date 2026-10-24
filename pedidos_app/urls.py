from django.urls import path
from . import views

app_name = "pedidos"

urlpatterns = [
    path(
        "processar_pedido/",
        views.processar_pedido,
        name="Processar Pedido"
    ),
]