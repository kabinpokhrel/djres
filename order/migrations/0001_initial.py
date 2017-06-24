# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=64)),
                ('po_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('delivery_location', models.TextField(max_length=500, null=True)),
                ('delivery_contact', models.CharField(blank=True, max_length=20, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
        ),
    ]