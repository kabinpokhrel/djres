# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-22 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_deliverychallan_issue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverychallan',
            name='challan_number',
            field=models.CharField(default='s', max_length=250),
            preserve_default=False,
        ),
    ]
