# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_info_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='smart',
            name='time',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
