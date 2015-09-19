# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20150606_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetype',
            name='type_comment',
            field=models.CharField(default=datetime.date(2015, 6, 9), max_length=200),
            preserve_default=False,
        ),
    ]
