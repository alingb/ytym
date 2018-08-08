# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0004_auto_20170808_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='exclusion_phase',
            field=models.CharField(max_length=250, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe9\x98\xb6\xe6\xae\xb5', choices=[(b'1', b'\xe5\xa4\x84\xe7\x90\x86\xe4\xb8\xad'), (b'2', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')]),
        ),
    ]
