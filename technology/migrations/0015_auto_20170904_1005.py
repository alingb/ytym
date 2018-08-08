# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0014_auto_20170811_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='error',
            options={'verbose_name': 'fault', 'verbose_name_plural': 'bugsystem'},
        ),
        migrations.AddField(
            model_name='error',
            name='sn',
            field=models.CharField(default='asasd', max_length=250, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81sn'),
            preserve_default=False,
        ),
    ]
