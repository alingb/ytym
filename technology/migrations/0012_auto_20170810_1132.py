# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0011_auto_20170809_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='bug_record',
            field=models.TextField(verbose_name=b'BUG\xe8\xae\xb0\xe5\xbd\x95', blank=True),
        ),
    ]
