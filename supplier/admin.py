from django.contrib import admin
from models.supplier import Supplier
from models.contact_person import ContactPerson

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'website')
    search_fields = ('name', 'address', 'website')
    list_filter = ('is_active',)

@admin.register(ContactPerson)
class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('is_active', 'role')
    autocomplete_fields = ('supplier',)
    raw_id_fields = ('supplier',)
    readonly_fields = ('created_at', 'updated_at')


