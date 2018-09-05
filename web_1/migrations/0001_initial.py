# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('statname', models.CharField(default=b'wait', unique=True, max_length=50, choices=[(b'run', b'run'), (b'stop', b'stop'), (b'poweroff', b'poweroff'), (b'bmcLogClear', b'bmcLogClear')])),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('server_id', models.AutoField(serialize=False, primary_key=True)),
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
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('messege', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
                ('sn', models.CharField(default=b'no date', max_length=50)),
                ('status', models.CharField(default=b'wait', max_length=50, choices=[(b'run', b'run'), (b'stop', b'stop'), (b'poweroff', b'poweroff'), (b'bmcLogClear', b'bmcLogClear')])),
                ('cpu', models.CharField(max_length=150)),
                ('mem', models.CharField(max_length=150)),
                ('num', models.CharField(max_length=150)),
                ('hostname', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='stat',
            field=models.ManyToManyField(to='web.Stat', blank=True),
        ),
    ]
