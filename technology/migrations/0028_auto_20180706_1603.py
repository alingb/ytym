# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0027_auto_20180706_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='faeerror',
            name='record_update',
            field=models.TextField(max_length=500, verbose_name=b'\xe8\xae\xb0\xe5\xbd\x95\xe6\x9b\xb4\xe6\x96\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='faeerror',
            name='exclusion',
            field=models.CharField(max_length=500, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe7\x8a\xb6\xe6\x80\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='faeerror',
            name='exclusion_phase',
            field=models.CharField(max_length=500, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'1', b'\xe5\xa4\x84\xe7\x90\x86\xe4\xb8\xad'), (b'2', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')]),
        ),
    ]
