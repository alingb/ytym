# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_auto_20171027_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smart',
            name='sel',
            field=models.TextField(verbose_name=b'BMC\xe6\x97\xa5\xe5\xbf\x97'),
        ),
        migrations.AlterField(
            model_name='smart',
            name='smart_info',
            field=models.TextField(verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae'),
        ),
        migrations.AlterField(
            model_name='smart',
            name='time',
            field=models.CharField(max_length=150, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
    ]
