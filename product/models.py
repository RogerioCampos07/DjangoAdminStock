import uuid

from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'product_category'
        verbose_name = 'Categoria de Produto'
        verbose_name_plural = 'Categorias de Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'brand'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Batch(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='batches'
    )
    batch_code = models.CharField(max_length=100, unique=True)
    expiration_date = models.DateField()
    manufacturing_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'batch'
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'
        ordering = ['-manufacturing_date']

    def __str__(self):
        return f'{self.product.name} - {self.batch_code}'
    

    



class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.PROTECT, related_name='products'
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='products'
    )
    activate = models.BooleanField(default=True)
    supplier = models.ManyToManyField(
        'supplier.Supplier', related_name='products'
    )
    has_batch = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.brand.name})'

    class Meta:
        db_table = 'product'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
