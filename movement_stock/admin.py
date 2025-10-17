from django.contrib import admin
from django.http import HttpRequest

from .models import MovementStock


@admin.register(MovementStock)
class MovementStockAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'batch',
        'movement_type',
        'quantity',
        'document_ref',
        'created_at',
    )
    list_filter = ('movement_type', 'product__category', 'product__brand')
    search_fields = ('product__name', 'batch__batch_code')
    ordering = ('-created_at',)
    autocomplete_fields = ('product', 'batch')

    def get_readonly_fields(  # noqa: PLR6301
        self, request: HttpRequest, obj: MovementStock | None = None
    ) -> tuple[str, ...]:
        if obj:
            return ('product', 'batch', 'movement_type', 'quantity')
        return ()
