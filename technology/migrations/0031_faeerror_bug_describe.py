# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0030_auto_20180713_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='faeerror',
            name='bug_describe',
            field=models.TextField(default='null', max_length=500, verbose_name=b'BUG\xe7\xae\x80\xe8\xbf\xb0'),
            preserve_default=False,
        ),
    ]
