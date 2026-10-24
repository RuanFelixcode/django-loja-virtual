from django.db import models

# Create your models here.


class Servico(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='servicos')
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'

    def __str__(self):
        return self.titulo