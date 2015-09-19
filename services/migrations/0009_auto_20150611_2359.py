# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20150611_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_comment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='main_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='servicetype',
            old_name='type_comment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='servicetype',
            old_name='type_text',
            new_name='name',
        ),
    ]
