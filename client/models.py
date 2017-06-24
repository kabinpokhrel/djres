from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=250, unique=False)
    challan_prefix = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True)
    relation_id = models.CharField(max_length=64, editable=True)
    payment_terms = models.IntegerField(verbose_name="payment terms", null=True, blank=True)
    address = models.TextField(max_length=500, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.client_name


class OurCompany(models.Model):
    name = models.CharField(max_length=250, verbose_name="Your Company")
    slug = models.SlugField(max_length=500, unique=True)
    office_address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    pin_code = models.IntegerField(verbose_name="PIN Code")
    cst_tin_number = models.CharField(max_length=300, verbose_name="Company's CST & TIN Number")
    service_tax_number = models.CharField(max_length=200, verbose_name="Company's Service TAX Number")
    pan_number = models.CharField(max_length=60, verbose_name="Company's PAN Number")

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name

    def company_address(self):
        return '{},{}, {}'.format(self.office_address, self.city, self.pin_code)
