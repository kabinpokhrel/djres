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
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Project Description')),
                ('deadline', models.DateField(verbose_name='Deadline')),
                ('quantity', models.IntegerField()),
                ('UOM', models.CharField(choices=[('MTR', 'Meter'), ('KG', 'Kilogram'), ('GRAM', 'Gram'), ('SFT', 'Square Feet'), ('RMT', 'Running Meter'), ('NOs', 'Number(s)'), ('EA', 'Each'), ('LTR', 'Litre'), ('BOX', 'Box(s)'), ('LOT', 'Lot(s)'), ('JOB', 'Job(s)')], default='Nos', max_length=10)),
                ('line_value', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.PurchaseOrder')),
            ],
        ),
    ]
