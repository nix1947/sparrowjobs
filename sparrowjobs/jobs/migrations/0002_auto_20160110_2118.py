# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobcategory',
            options={'verbose_name_plural': 'Job Categories'},
        ),
    ]