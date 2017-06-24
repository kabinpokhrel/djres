from django.db import models
from order.models import PurchaseOrder
from invoice.models import DeliveryChallan

DEFAULT_UNIT = 'Nos'
UNIT_CHOICES = (
    ('MTR', 'Meter'),
    ('KG', 'Kilogram'),
    ('GRAM', 'Gram'),
    ('SFT', 'Square Feet'),
    ('RMT', 'Running Meter'),
    ('NOs', 'Number(s)'),
    ('EA', 'Each'),
    ('LTR', 'Litre'),
    ('BOX', 'Box(s)'),
    ('LOT', 'Lot(s)'),
    ('JOB', 'Job(s)'))


class LineItem(models.Model):
    description = models.TextField(verbose_name='Line Description', max_length=1000, blank=True, editable=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    UOM = models.CharField(max_length=10, choices=UNIT_CHOICES, default=DEFAULT_UNIT)
    line_value = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.description


class DeliveryChallanItem(models.Model):
    delivery_challan = models.ForeignKey(DeliveryChallan, on_delete=models.CASCADE)
    particular = models.CharField(max_length=1000)
    quantity = models.IntegerField(blank=True, null=True, default=1)
    mou = models.CharField(max_length=20, choices=UNIT_CHOICES, default=DEFAULT_UNIT)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.delivery_challan.challan_number
