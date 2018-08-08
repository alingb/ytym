# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0017_smartinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartinfo',
            name='model',
        ),
        migrations.RemoveField(
            model_name='smartinfo',
            name='size',
        ),
        migrations.AddField(
            model_name='smartinfo',
            name='sel',
            field=models.TextField(default='q', verbose_name=b'BMC\xe6\x97\xa5\xe5\xbf\x97'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smartinfo',
            name='sn_1',
            field=models.CharField(default='a', max_length=250, verbose_name=b'sn'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smartinfo',
            name='sn',
            field=models.CharField(max_length=250, verbose_name=b'sn'),
        ),
    ]
