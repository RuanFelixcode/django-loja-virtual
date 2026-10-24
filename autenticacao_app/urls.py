from django.urls import path
from .views import VRegistro,encerar_sessao,pagina_login


urlpatterns = [path('',VRegistro.as_view(), name='Autenticar Usuario'),
path('encerar_sessao',encerar_sessao, name='Encerar Sessao'),
path('pagina_login',pagina_login, name='Pagina Login'),

]