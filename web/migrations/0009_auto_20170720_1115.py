# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20170706_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='messege',
            new_name='message',
        ),
    ]
