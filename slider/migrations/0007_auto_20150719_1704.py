# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0006_auto_20150630_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': 'Слайдер изображений', 'verbose_name': 'Изображение'},
        ),
        migrations.AlterField(
            model_name='slider',
            name='comment',
            field=models.CharField(blank=True, max_length=100, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='slider', verbose_name='Изображение'),
        ),
    ]
