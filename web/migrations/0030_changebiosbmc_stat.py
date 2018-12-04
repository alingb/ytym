# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_hostcheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='changebiosbmc',
            name='stat',
            field=models.CharField(max_length=250, verbose_name=b'status', blank=True),
        ),
    ]
