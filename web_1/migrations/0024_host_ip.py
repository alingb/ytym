# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_auto_20171123_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='ip',
            field=models.CharField(max_length=550, blank=True),
        ),
    ]
