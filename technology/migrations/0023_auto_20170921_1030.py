# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0022_error_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='error',
            name='exclusione',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe9\x98\xb6\xe6\xae\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='error',
            name='level',
            field=models.CharField(max_length=500, verbose_name=b'BUG\xe7\xad\x89\xe7\xba\xa7', blank=True),
        ),
    ]
