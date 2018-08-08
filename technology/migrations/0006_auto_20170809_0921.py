# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0005_auto_20170808_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='configuration_information',
            field=models.CharField(max_length=250, verbose_name=b'\xe9\x85\x8d\xe7\xbd\xae\xe4\xbf\xa1\xe6\x81\xaf'),
        ),
        migrations.AlterField(
            model_name='error',
            name='phenomenon_description',
            field=models.CharField(max_length=250, verbose_name=b'bug\xe7\x8e\xb0\xe8\xb1\xa1\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='error',
            name='step_description',
            field=models.CharField(max_length=250, verbose_name=b'bug\xe4\xba\xa7\xe7\x94\x9f\xe6\xad\xa5\xe9\xaa\xa4\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='error',
            name='suggested_view',
            field=models.CharField(max_length=250, verbose_name=b'\xe5\xbb\xba\xe8\xae\xae\xe7\x9c\x8b\xe6\xb3\x95'),
        ),
    ]
