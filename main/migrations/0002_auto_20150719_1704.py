# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maintext',
            options={'verbose_name_plural': 'Текст главной страницы', 'verbose_name': 'текст'},
        ),
        migrations.AddField(
            model_name='maintext',
            name='image',
            field=models.ImageField(upload_to='main', default=datetime.datetime(2015, 7, 19, 14, 4, 12, 31760, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maintext',
            name='head',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='maintext',
            name='text',
            field=models.CharField(max_length=900, verbose_name='Текст'),
        ),
    ]
