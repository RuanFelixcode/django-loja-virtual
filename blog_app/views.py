from django.shortcuts import render
from .models import Post, Categoria


# Create your views here.


def blog(request):
    categorias = Categoria.objects.all()

    return render(
        request,
        'blog/blog.html',
        {
            'categorias': categorias,
            'pagina': 'blog'
        }
    )


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)

    return render(
        request,
        'blog/categoria.html',
        {
            'categoria': categoria,
            'posts': posts,
            'pagina': 'blog'
        }
    )