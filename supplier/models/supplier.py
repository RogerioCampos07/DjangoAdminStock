from django.db import models


# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nome')
    description = models.TextField(
        blank=True, null=True, verbose_name='Descrição'
    )
    address = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Endereço'
    )
    website = models.URLField(blank=True, null=True, verbose_name='Site')
    is_active = models.BooleanField(
        default=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'supplier'
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['name']

    def __str__(self):
        return self.name
