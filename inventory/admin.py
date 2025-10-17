from django.contrib import admin
from django.http import HttpRequest

from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'batch', 'quantity')
    list_filter = ('product__category', 'product__brand')
    search_fields = ('product__name', 'batch__batch_code')
    ordering = ('product__name',)
    readonly_fields = ('product', 'batch', 'quantity')

    @staticmethod
    def has_add_permission(request: HttpRequest) -> bool:
        return False

    @staticmethod
    def has_delete_permission(
        request: HttpRequest, obj: Inventory | None = None
    ) -> bool:
        return False
