# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20150606_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelist',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
