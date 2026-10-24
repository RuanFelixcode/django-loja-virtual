from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='imagem_produto',null = True,blank = True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
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
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    def __str__(self):
        return self.nome

