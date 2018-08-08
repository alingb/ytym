# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0003_auto_20170808_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='product_name_other',
            field=models.CharField(max_length=250, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
    ]
