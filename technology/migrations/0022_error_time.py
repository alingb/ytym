# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0021_auto_20170915_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='error',
            name='time',
            field=models.CharField(max_length=250, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
    ]
