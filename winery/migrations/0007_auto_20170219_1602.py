# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winery', '0006_auto_20170217_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='award',
            field=models.ImageField(null=True, upload_to='/award'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='/company'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='/product'),
        ),
    ]
