"""
URL configuration for projeto_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('projeto_web_app.urls')),
    path('servicos/',include('servicos_app.urls')),
    path('blog/',include('blog_app.urls')),
    path('contato/',include('contato_app.urls')),
    path('loja/',include('loja_app.urls')),
    path('carro/',include('carro_app.urls')),
    path('autenticar_usuario/',include('autenticacao_app.urls')),
    path("processar_pedido/",include('pedidos_app.urls')),
]
