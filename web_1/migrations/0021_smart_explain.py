# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_smart_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='smart',
            name='explain',
            field=models.CharField(max_length=550, verbose_name=b'\xe8\xaf\xb4\xe6\x98\x8e', blank=True),
        ),
    ]
