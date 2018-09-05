# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_changebiosbmc_fru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='changebiosbmc',
            name='number',
        ),
    ]
