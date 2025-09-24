from django.db import models

from supplier.models import Supplier


class ContactPerson(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='contact_persons',
        verbose_name='Fornecedor',
    )
    name = models.CharField(max_length=255, verbose_name='Nome')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    role = models.CharField(
        max_length=100, default='Fornecedor', verbose_name='Cargo'
    )
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contact_person'
        verbose_name = 'Pessoa de Contato'
        verbose_name_plural = 'Pessoas de Contato'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.supplier.name})'
