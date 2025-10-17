from django.contrib import admin

from .models import Batch, Brand, Product, ProductCategory


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'batch_code',
        'expiration_date',
        'manufacturing_date',
    )
    search_fields = ('product__name', 'batch_code')
    ordering = ('product__name',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'category',
        'price',
        'activate',
    )
    list_filter = ('brand', 'category', 'activate')
    search_fields = ('name', 'brand__name', 'category__name')
    ordering = ('name',)
    filter_horizontal = ('supplier',)
    fieldsets = (
        (
            'Informações principais',
            {
                'fields': (
                    'name',
                    'description',
                    'category',
                    'brand',
                    'supplier',
                    'activate',
                )
            },
        ),
        ('Preço de compra', {'fields': ('price',)}),
        (
            'Datas',
            {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)},
        ),
    )
    readonly_fields = ('created_at', 'updated_at')
