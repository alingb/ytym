# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0023_auto_20170921_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='error',
            old_name='exclusione',
            new_name='exclusion',
        ),
    ]
