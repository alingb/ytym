# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20170614_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='bios',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='host',
            name='bmc',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='host',
            name='cpu',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='host',
            name='disk',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='host',
            name='family',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='host',
            name='mac',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='host',
            name='memory',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='host',
            name='name1',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='host',
            name='network',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='host',
            name='raid',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='host',
            name='sn',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='host',
            name='sn_1',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='host',
            name='status',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='host',
            name='stress_test',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='bios',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='bmc',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='cpu',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='disk',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='family',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='hostname',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='mac',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='memory',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='name1',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='network',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='raid',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='sn',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='sn_1',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='status',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='hostcheck',
            name='stress_test',
            field=models.CharField(max_length=250),
        ),
    ]