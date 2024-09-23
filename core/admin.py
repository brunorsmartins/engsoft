from django.contrib import admin
from .models import Sprint, Daily

@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_fim', 'gerente', 'nota_final')
    search_fields = ('nome', 'descricao')
    list_filter = ('gerente', 'data_inicio', 'data_fim')
    date_hierarchy = 'data_inicio'

@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
    list_display = ('sprint', 'data', 'descricao')
    search_fields = ('sprint__nome', 'descricao')
    list_filter = ('sprint', 'data')
    date_hierarchy = 'data'
