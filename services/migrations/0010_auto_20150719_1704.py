# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20150611_2359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicetype',
            options={'verbose_name_plural': 'Услуги', 'verbose_name': 'Услугу'},
        ),
    ]
