# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170602_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostCheck',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('sn', models.CharField(max_length=50)),
                ('sn_1', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=250)),
                ('time', models.DateField()),
                ('cpu', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('disk', models.CharField(max_length=250)),
                ('raid', models.CharField(max_length=50)),
                ('network', models.CharField(max_length=250)),
                ('mac', models.CharField(max_length=250)),
                ('bios', models.CharField(max_length=50)),
                ('bmc', models.CharField(max_length=50)),
                ('sel', models.TextField()),
                ('stress_test', models.CharField(max_length=50)),
                ('hostname', models.CharField(max_length=50)),
                ('disk_num', models.IntegerField()),
                ('messege', models.TextField()),
                ('fru', models.TextField()),
            ],
        ),
    ]
