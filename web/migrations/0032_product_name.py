# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0031_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=datetime.datetime(2018, 6, 11, 6, 37, 59, 3408, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
    ]
