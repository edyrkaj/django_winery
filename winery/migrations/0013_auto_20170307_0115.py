# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('winery', '0012_auto_20170307_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_manager', models.BooleanField(default='False')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='winery.Company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='winery.Users')),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='client',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
