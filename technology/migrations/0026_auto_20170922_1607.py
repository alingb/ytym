# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0025_auto_20170922_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='test_model',
            field=models.TextField(max_length=500, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe6\x8e\xaa\xe6\x96\xbd', blank=True),
        ),
    ]
