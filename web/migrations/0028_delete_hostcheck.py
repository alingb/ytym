# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_remove_changebiosbmc_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HostCheck',
        ),
    ]
