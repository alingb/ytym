# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0009_auto_20170809_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='customer',
            field=models.CharField(max_length=250, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='discovery',
            field=models.CharField(max_length=250, verbose_name=b'\xe5\x8f\x91\xe7\x8e\xb0\xe9\x80\x94\xe5\xbe\x84', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='email',
            field=models.CharField(max_length=250, verbose_name=b'\xe6\x8a\x84\xe9\x80\x81\xe4\xba\xba\xe5\x91\x98', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='product',
            field=models.CharField(max_length=250, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='project',
            field=models.CharField(max_length=250, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='test_person',
            field=models.CharField(max_length=250, verbose_name=b'\xe6\xb5\x8b\xe8\xaf\x95\xe4\xba\xba\xe5\x91\x98', blank=True),
        ),
    ]
