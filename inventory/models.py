from django.db import models


class Inventory(models.Model):
    product = models.ForeignKey(
        'product.Product', on_delete=models.PROTECT, related_name='inventory'
    )
    batch = models.ForeignKey(
        'product.Batch',
        on_delete=models.PROTECT,
        related_name='inventory',
        blank=True,
        null=True,
    )
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'inventory'
        verbose_name = 'Estoque'
        unique_together = ('product', 'batch')

    def __str__(self):
        batch_info = self.batch.batch_code if self.batch else 'Sem Lote'
        return f'{self.product.name} - {batch_info}: {self.quantity}'
