# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_host_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeBiosBmc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=250, verbose_name=b'sn')),
                ('sn_1', models.CharField(max_length=250, verbose_name=b'sn_1')),
                ('ip', models.CharField(max_length=250, verbose_name=b'ip')),
                ('bios', models.CharField(max_length=250, verbose_name=b'bios')),
                ('bmc', models.CharField(max_length=250, verbose_name=b'bmc')),
                ('name', models.CharField(max_length=250, verbose_name=b'name')),
                ('family', models.CharField(max_length=250, verbose_name=b'family')),
                ('number', models.IntegerField(verbose_name=b'number')),
            ],
        ),
    ]
