# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0016_auto_20170914_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=250, verbose_name=b'\xe7\xa1\xac\xe7\x9b\x98sn')),
                ('model', models.CharField(max_length=250, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7')),
                ('size', models.CharField(max_length=250, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7')),
                ('data', models.TextField(verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae')),
            ],
        ),
    ]
