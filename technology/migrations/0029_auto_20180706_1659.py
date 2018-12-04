# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0028_auto_20180706_1603'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='error',
            options={'verbose_name': 'product_fault', 'verbose_name_plural': 'product_bugsystem'},
        ),
        migrations.AlterModelOptions(
            name='faeerror',
            options={'verbose_name': 'fae_fault', 'verbose_name_plural': 'fae_bugsystem'},
        ),
    ]
