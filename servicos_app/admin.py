from django.contrib import admin

# Register your models here.
from .models import Servico


class ServicoAdmin(admin.ModelAdmin):
    readonly_fields = ('criado','atualizado')


admin.site.register(Servico)