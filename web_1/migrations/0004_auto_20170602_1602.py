# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_hostcheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='name1',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostcheck',
            name='name1',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
    ]
