# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_date', models.DateField(verbose_name='PO date')),
                ('invoice_date', models.DateField(verbose_name='Invoice date')),
                ('invoice_issued', models.BooleanField(verbose_name='Is Invoiced Sent?')),
                ('invoiced_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('taxable', models.BooleanField()),
                ('gst_value', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('payment_due_date', models.DateField(verbose_name='Payment Deu')),
                ('payment_received', models.BooleanField(verbose_name='Is Payment Received?')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.PurchaseOrder')),
            ],
        ),
    ]
