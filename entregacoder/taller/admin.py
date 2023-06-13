from django.contrib import admin
from .models import Lider, Operario, Herramienta, Consumible

@admin.register(Herramienta)
class HerramientaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'rastreo',
        'operario',
    ]
    search_fields = ('nombre',)
    list_editable = ('operario',)
    ordering = ('nombre', 'rastreo',)

admin.site.register(Lider)
admin.site.register(Operario)
#admin.site.register(Herramienta)
admin.site.register(Consumible)
