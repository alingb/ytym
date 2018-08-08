# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20170922_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
