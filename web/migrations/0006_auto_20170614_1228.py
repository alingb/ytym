# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20170607_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='raid',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='raid',
            field=models.CharField(max_length=250),
        ),
    ]
