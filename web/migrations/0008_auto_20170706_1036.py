# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20170705_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='mac_addr',
            field=models.CharField(default='', max_length=550),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostcheck',
            name='mac_addr',
            field=models.CharField(default='none', max_length=550),
            preserve_default=False,
        ),
    ]
