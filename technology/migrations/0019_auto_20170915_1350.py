# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0018_auto_20170915_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartinfo',
            name='data',
            field=models.TextField(verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae', blank=True),
        ),
        migrations.AlterField(
            model_name='smartinfo',
            name='sel',
            field=models.TextField(verbose_name=b'BMC\xe6\x97\xa5\xe5\xbf\x97', blank=True),
        ),
    ]
