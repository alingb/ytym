# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20170919_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='enclosure',
            field=models.FileField(upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='hostcheck',
            name='enclosure',
            field=models.FileField(upload_to=b'', blank=True),
        ),
    ]
