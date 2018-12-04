# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0029_auto_20180706_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faeerror',
            name='resolvent',
            field=models.TextField(verbose_name=b'\xe8\xa7\xa3\xe5\x86\xb3\xe6\x96\xb9\xe6\xb3\x95'),
        ),
    ]
