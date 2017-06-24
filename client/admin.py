from django.contrib import admin

from .models import Client, OurCompany


class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("client_name",)}
    fieldsets = [
        ('Client Info', {'fields': ['client_name', 'relation_id', 'payment_terms', 'slug']}),
        ('Address Information', {'fields': ['address']}),
    ]
    list_display = ('client_name', 'relation_id', 'payment_terms', 'challan_prefix', 'address')


class OurCompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'company_address')



admin.site.register(OurCompany, OurCompanyAdmin)
admin.site.register(Client, ClientAdmin)
