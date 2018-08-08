# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0013_error_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='phenomenon_description',
            field=models.CharField(max_length=500, verbose_name=b'bug\xe8\xaf\xa6\xe7\xbb\x86\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='error',
            name='step_description',
            field=models.CharField(max_length=500, verbose_name=b'bug\xe5\x8f\x91\xe7\x94\x9f\xe6\xad\xa5\xe9\xaa\xa4'),
        ),
    ]
