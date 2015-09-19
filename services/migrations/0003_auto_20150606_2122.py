# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20150606_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicetype',
            name='price_view',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='work_view',
        ),
    ]
