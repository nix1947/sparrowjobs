# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_size',
            field=models.CharField(blank=True, default='10-20', max_length=6),
        ),
    ]
