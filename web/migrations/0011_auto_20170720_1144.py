# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20170720_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='boot_time',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostcheck',
            name='boot_time',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
