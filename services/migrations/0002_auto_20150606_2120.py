# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricelist',
            old_name='price_type',
            new_name='main_type',
        ),
        migrations.AddField(
            model_name='pricelist',
            name='service_comment',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicetype',
            name='price_view',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicetype',
            name='work_view',
            field=models.CharField(default=datetime.date(2015, 6, 6), max_length=200),
            preserve_default=False,
        ),
    ]
