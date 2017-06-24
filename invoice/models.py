from django.db import models
from order.models import PurchaseOrder


class Invoice(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    po_date = models.DateField(verbose_name="PO date")
    invoice_date = models.DateField(verbose_name="Invoice date")
    invoice_issued = models.BooleanField(verbose_name="Is Invoiced Sent?")
    invoiced_amount = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=2)
    taxable = models.BooleanField()
    gst_value = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=2)
    estimated_payment_date = models.DateField(verbose_name="Estimated Payment Date")
    payment_received = models.BooleanField(verbose_name="Is Payment Received?")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.purchase_order.po_number


class DeliveryChallan(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    challan_number = models.CharField(max_length=250)
    issue_date = models.DateField(verbose_name='DC Issued Date', null=True, blank=True)
    goods_sent_through = models.CharField(max_length=250, blank=True, null=True)
    work_order_number = models.CharField(max_length=250, blank=True, null=True)
    work_order_date = models.DateField(verbose_name='Your work order date')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.purchase_order.po_number