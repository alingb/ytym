# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0024_auto_20170921_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='test_model',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe6\x8e\xaa\xe6\x96\xbd', blank=True),
        ),
    ]
