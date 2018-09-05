# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20170724_1700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': '\u8fd0\u884c', 'verbose_name_plural': '\u8fd0\u884c\u72b6\u6001'},
        ),
        migrations.AlterModelOptions(
            name='host',
            options={'verbose_name': '\u670d\u52a1\u5668\u4fe1\u606f', 'verbose_name_plural': '\u8001\u5316\u6d4b\u8bd5\u7cfb\u7edf'},
        ),
        migrations.AlterModelOptions(
            name='hostcheck',
            options={'verbose_name': '\u670d\u52a1\u5668\u4fe1\u606f', 'verbose_name_plural': '\u8fd1\u671f\u670d\u52a1\u5668\u4fe1\u606f'},
        ),
    ]
