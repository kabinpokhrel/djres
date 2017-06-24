from django.contrib import admin
from .models import LineItem, DeliveryChallanItem


class LineItemAdmin(admin.ModelAdmin):
    list_display = ('purchase_order', 'line_value')


class DeliveryChallanItemAdmin(admin.ModelAdmin):
    list_display = (
        'delivery_challan',
        'particular',
        'quantity',
        'mou')

admin.site.register(LineItem, LineItemAdmin)
admin.site.register(DeliveryChallanItem, DeliveryChallanItemAdmin)