# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_servicetype_type_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(max_length=200)),
                ('service_comment', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=50)),
                ('main_type', models.ForeignKey(to='services.ServiceType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='pricelist',
            name='main_type',
        ),
        migrations.DeleteModel(
            name='PriceList',
        ),
    ]
