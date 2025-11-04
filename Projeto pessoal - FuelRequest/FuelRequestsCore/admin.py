from django.contrib import admin
from . models import  cliente, plano

# Register your models here.

class planoAdmin(admin.ModelAdmin):
    list_display=('nome', 'preco', 'vendas')


class clienteAdmin(admin.ModelAdmin):
    list_display=('nome', 'sobrenome', 'email')


admin.site.register(cliente, clienteAdmin)
admin.site.register(plano, planoAdmin)
