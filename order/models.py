from django.db import models
from client.models import Client


class PurchaseOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=64, editable=True)
    po_amount = models.DecimalField(blank=True ,null=True, max_digits=15, decimal_places=2)
    deadline = models.DateField(verbose_name='Deadline', null=True, blank=True)
    delivery_location = models.TextField(max_length=500, blank=False, null=True)
    delivery_contact = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return '{}-{}'.format(self.client.client_name, self.po_number)

