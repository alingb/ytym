# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0019_auto_20170915_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smartinfo',
            old_name='data',
            new_name='smart_info',
        ),
        migrations.AlterField(
            model_name='smartinfo',
            name='sn_1',
            field=models.CharField(max_length=250, verbose_name=b'sn_1'),
        ),
    ]
