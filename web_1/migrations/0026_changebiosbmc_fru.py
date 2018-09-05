# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_changebiosbmc'),
    ]

    operations = [
        migrations.AddField(
            model_name='changebiosbmc',
            name='fru',
            field=models.CharField(max_length=250, verbose_name=b'fru_info', blank=True),
        ),
    ]
