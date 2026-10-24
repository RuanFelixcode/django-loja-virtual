from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome



class Post(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='blog',null = True,blank = True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )


    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.titulo