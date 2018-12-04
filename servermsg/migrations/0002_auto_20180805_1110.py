# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servermsg', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servermessage',
            options={},
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='bios',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='bmc',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='boot_time',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='disk',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='disk_num',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='enclosure',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='family',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='fru',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='hostname',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='mac',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='mac_addr',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='message',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='name1',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='network',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='raid',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='sel',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='smart_info',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='sn',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='sn1',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='status',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='stress_test',
        ),
        migrations.RemoveField(
            model_name='servermessage',
            name='time',
        ),
        migrations.AlterField(
            model_name='servermessage',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
