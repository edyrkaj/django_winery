# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winery', '0002_auto_20170202_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='award',
            field=models.ImageField(null=True, upload_to='C:/Users/Admin/Desktop/teste/jquerymobile/images/test/award'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='C:/Users/Admin/Desktop/teste/jquerymobile/images/test/company'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='C:/Users/Admin/Desktop/teste/jquerymobile/images/test/product'),
        ),
    ]
