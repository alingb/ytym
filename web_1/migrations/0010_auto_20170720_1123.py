# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20170720_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='messege',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='hostcheck',
            old_name='messege',
            new_name='message',
        ),
    ]
