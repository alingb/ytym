# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_smart_explain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='enclosure',
            field=models.FileField(upload_to=b'', verbose_name=b'breakin', blank=True),
        ),
    ]
