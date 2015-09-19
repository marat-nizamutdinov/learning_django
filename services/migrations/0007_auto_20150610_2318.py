# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20150610_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='main_type',
            field=models.ForeignKey(related_name=b'main_type', to='services.ServiceType'),
        ),
    ]
