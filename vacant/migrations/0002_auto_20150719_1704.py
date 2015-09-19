# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacant',
            options={'verbose_name_plural': 'Вакансии', 'verbose_name': 'Вакансию'},
        ),
        migrations.AlterField(
            model_name='vacant',
            name='vacancy',
            field=models.CharField(max_length=100, verbose_name='Вакансия'),
        ),
    ]
