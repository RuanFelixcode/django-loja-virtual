from django.contrib import admin
from .models import Categoria, Produto
# Register your models here.




class ProdutoAdmin(admin.ModelAdmin):
    readonly_fields = ('criado', 'atualizado')


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)