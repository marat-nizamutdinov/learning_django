# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('person_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('person_last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('person_phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('person_mail', models.EmailField(max_length=40, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
