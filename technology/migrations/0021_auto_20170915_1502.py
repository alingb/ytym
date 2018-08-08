# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0020_auto_20170915_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=250, verbose_name=b'sn')),
                ('sn_1', models.CharField(max_length=250, verbose_name=b'sn_1')),
                ('sel', models.TextField(verbose_name=b'BMC\xe6\x97\xa5\xe5\xbf\x97', blank=True)),
                ('smart_info', models.TextField(verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae', blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SmartInfo',
        ),
    ]
