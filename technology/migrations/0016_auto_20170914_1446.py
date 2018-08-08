# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0015_auto_20170904_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='bug_describe',
            field=models.TextField(max_length=500, verbose_name=b'BUG\xe7\xae\x80\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='error',
            name='phenomenon_description',
            field=models.CharField(max_length=500, verbose_name=b'bug\xe7\x8e\xb0\xe8\xb1\xa1\xe8\xaf\xa6\xe7\xbb\x86\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='error',
            name='test_model',
            field=models.TextField(max_length=500, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe6\x8e\xaa\xe6\x96\xbd', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='test_site',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\x8f\x91\xe7\x94\x9f\xe5\x9c\xb0\xe7\x82\xb9', blank=True),
        ),
    ]
