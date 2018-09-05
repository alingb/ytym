# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_smart'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='smart_info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hostcheck',
            name='smart_info',
            field=models.TextField(blank=True),
        ),
    ]
