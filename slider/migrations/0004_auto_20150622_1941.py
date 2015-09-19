# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0003_auto_20150621_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='comment',
            field=models.CharField(max_length=100),
        ),
    ]
