# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20170720_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
