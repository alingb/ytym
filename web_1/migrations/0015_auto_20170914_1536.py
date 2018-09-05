# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20170914_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='message',
            field=models.FileField(upload_to=b'', blank=True),
        ),
    ]
