# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0004_auto_20150622_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='comment',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
