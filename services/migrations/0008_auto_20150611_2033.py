# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20150610_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='main_type',
            field=models.ForeignKey(to='services.ServiceType'),
        ),
    ]
