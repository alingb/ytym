# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20170602_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='sn',
            field=models.CharField(default=b'no date', max_length=150),
        ),
    ]
