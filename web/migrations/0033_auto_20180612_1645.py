# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='orders',
        ),
        migrations.AddField(
            model_name='product',
            name='orders',
            field=models.ManyToManyField(to='web.Host'),
        ),
    ]
