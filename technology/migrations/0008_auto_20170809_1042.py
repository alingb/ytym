# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0007_auto_20170809_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='customer_name',
            field=models.CharField(max_length=250, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0', choices=[(b'1', b'\xe9\x94\x90\xe6\x8d\xb7'), (b'2', b'\xe6\xb7\xb1\xe4\xbf\xa1\xe6\x9c\x8d'), (b'3', b'\xe4\xb8\x89\xe7\x9b\x9f'), (b'other', b'\xe5\x85\xb6\xe4\xbb\x96')]),
        ),
        migrations.AlterField(
            model_name='error',
            name='discovery_phase',
            field=models.CharField(max_length=250, verbose_name=b'\xe5\x8f\x91\xe7\x8e\xb0\xe9\x80\x94\xe5\xbe\x84', choices=[(b'1', b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x86\x85\xe9\x83\xa8'), (b'2', b'\xe5\xae\xa2\xe6\x88\xb7'), (b'other', b'\xe5\x85\xb6\xe4\xbb\x96')]),
        ),
    ]
