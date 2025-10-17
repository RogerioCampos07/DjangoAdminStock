from django.core.exceptions import ValidationError
from django.db import models


class MovementStock(models.Model):
    class MovementTypes(models.TextChoices):
        INPUT = 'IN', 'Entrada'
        OUTPUT = 'OUT', 'Saída'
        ADJUSTMENT = 'ADJ', 'Ajuste'

    product = models.ForeignKey(
        'product.Product', on_delete=models.PROTECT, related_name='movements'
    )
    batch = models.ForeignKey(
        'product.Batch',
        on_delete=models.PROTECT,
        related_name='movements',
        blank=True,
        null=True,
    )
    movement_type = models.CharField(
        max_length=3, choices=MovementTypes.choices
    )  # noqa E501
    quantity = models.PositiveIntegerField()
    document_ref = models.CharField(
        'Documento de Referência',
        max_length=255,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'movement_stock'
        verbose_name = 'Movimento de Estoque'
        verbose_name_plural = 'Movimentos de Estoque'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.get_movement_type_display()} - {self.product.name} ({self.quantity})'  # noqa E501

    def clean(self):
        super().clean()
        if self.batch and not self.product.has_batch:
            msg = 'Este produto não está configurado para controle de lote.'
            raise ValidationError({'batch': msg})
        if self.product.has_batch and not self.batch:
            msg = 'Este produto requer a especificação de um lote.'
            raise ValidationError({'batch': msg})
