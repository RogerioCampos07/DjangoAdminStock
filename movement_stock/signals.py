from django.core.exceptions import ValidationError
from django.db.models import F
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from inventory.models import Inventory

from .models import MovementStock


@receiver(pre_save, sender=MovementStock)
def validate_stock_availability(sender, instance, **kwargs):
    """Impede que uma movimentação de saída deixe o estoque negativo."""
    if instance.pk:  # Ignora na criação, pois o post_save ainda não rodou
        return

    if instance.movement_type == MovementStock.MovementTypes.OUTPUT:
        try:
            inventory = Inventory.objects.get(
                product=instance.product, batch=instance.batch
            )
            if inventory.quantity < instance.quantity:
                raise ValidationError(
                    f'Estoque insuficiente. Disponível: {inventory.quantity}'
                )
        except Inventory.DoesNotExist:
            raise ValidationError('Estoque insuficiente. Disponível: 0')


@receiver(post_save, sender=MovementStock)
def update_inventory(sender, instance, created, **kwargs):
    if not created:
        return

    inventory, _ = Inventory.objects.get_or_create(
        product=instance.product,
        batch=instance.batch,
        defaults={'quantity': 0},
    )

    if instance.movement_type == MovementStock.MovementTypes.INPUT:
        inventory.quantity = F('quantity') + instance.quantity
    elif instance.movement_type == MovementStock.MovementTypes.OUTPUT:
        inventory.quantity = F('quantity') - instance.quantity
    elif instance.movement_type == MovementStock.MovementTypes.ADJUSTMENT:
        inventory.quantity = instance.quantity

    inventory.save()
