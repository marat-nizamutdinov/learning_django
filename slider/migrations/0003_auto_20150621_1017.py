# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import sorl.thumbnail.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_auto_20150614_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='comment',
            field=models.CharField(max_length=150, default=datetime.datetime(2015, 6, 21, 7, 17, 12, 234011, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='slider'),
        ),
    ]
