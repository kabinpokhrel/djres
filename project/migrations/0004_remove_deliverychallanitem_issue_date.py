# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 09:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_remove_deliverychallanitem_purchase_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverychallanitem',
            name='issue_date',
        ),
    ]