# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0033_auto_20180612_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='orders',
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
