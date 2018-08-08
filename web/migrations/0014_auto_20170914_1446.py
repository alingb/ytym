# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20170904_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='message',
            field=models.FilePathField(path=b'/data/mysql'),
        ),
    ]
