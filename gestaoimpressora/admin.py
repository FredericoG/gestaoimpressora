from django.contrib import admin
from .models import Equipamento, Item, Troca, Contador

class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'serial', 'tipo']
    search_fields = ['descricao', 'serial']
    list_filter = ['tipo']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'tipo', 'descricao', 'custo', 'durabilidade']
    search_fields = ['codigo', 'descricao']
    list_filter = ['tipo']

class TrocaAdmin(admin.ModelAdmin):
    list_display = ['equipamento', 'item', 'quantidade', 'contador', 'data_troca']
    search_fields = ['equipamento__descricao', 'item__descricao']
    list_filter = ['data_troca']

class ContadorAdmin(admin.ModelAdmin):
    list_display = ['equipamento', 'contador', 'data']
    search_fields = ['equipamento__descricao']
    list_filter = ['data']

admin.site.register(Equipamento, EquipamentoAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Troca, TrocaAdmin)
admin.site.register(Contador, ContadorAdmin)
