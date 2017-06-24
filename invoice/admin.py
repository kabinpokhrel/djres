from django.contrib import admin
from .models import Invoice, DeliveryChallan
from project.models import DeliveryChallanItem


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['purchase_order',
                    'po_date',
                    'invoice_date',
                    'invoice_issued',
                    'invoiced_amount',
                    'taxable',
                    'gst_value',
                    'estimated_payment_date',
                    'payment_received']
    list_filter = ('taxable', 'purchase_order__po_number', 'payment_received')
    list_per_page = 50
    # readonly_fields = ('purchase_order',)


class DeliveryChallanItemInline(admin.StackedInline):
    model = DeliveryChallanItem
    extra = 1
    fieldsets = [
        (None, {'fields': ['delivery_challan', 'particular', 'quantity', 'mou']})
    ]


class DeliveryChallanAdmin(admin.ModelAdmin):
    list_display = ['purchase_order',
                    'challan_number',
                    'goods_sent_through',
                    'work_order_number',
                    'work_order_date',
                    'timestamp']
    fieldsets = [
        ('Client', {'fields': ['purchase_order', 'challan_number', 'issue_date']}),
        ('Delivery Details', {'fields': ['goods_sent_through', 'work_order_number', 'work_order_date']}),
    ]
    inlines = [DeliveryChallanItemInline]


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(DeliveryChallan, DeliveryChallanAdmin)
