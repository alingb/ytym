# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='num',
            field=models.IntegerField(verbose_name=b'bug\xe7\xbc\x96\xe5\x8f\xb7', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
