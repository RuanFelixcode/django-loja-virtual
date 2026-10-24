from django.contrib import admin
from .models import Categoria, Post
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('criado', 'atualizado')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('criado', 'atualizado')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)