# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subtitle',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
