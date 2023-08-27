from django.contrib import admin
from .models import Pedido, PedidoItem

class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        PedidoItemInline
    ]

# Register your models here.
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoItem)
