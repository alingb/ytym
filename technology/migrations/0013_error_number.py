# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0012_auto_20170810_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='error',
            name='number',
            field=models.CharField(max_length=50, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7', blank=True),
        ),
    ]
