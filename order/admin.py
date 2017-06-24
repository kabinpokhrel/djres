from django.contrib import admin
from .models import PurchaseOrder
from project.models import LineItem


class LineItemInline(admin.StackedInline):
    model = LineItem
    extra = 1
    fieldsets = [
        (None, {'fields': ['description']}),
        ('Quantity', {'fields': ['quantity', 'UOM', 'line_value']})
    ]


class PurchaseOrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('PO Against', {'fields': ['client', 'po_number', 'deadline']}),
        ('Delivery information', {'fields': ['delivery_location', 'delivery_contact']}),
    ]
    list_display = ('client', 'po_number', 'delivery_location', 'delivery_contact', 'deadline')
    inlines = [LineItemInline]
    list_filter = ('po_number', 'client__client_name')
    # list_display_links = None


admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
