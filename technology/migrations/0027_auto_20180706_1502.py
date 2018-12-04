# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0026_auto_20170922_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaeError',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(verbose_name=b'bug\xe7\xbc\x96\xe5\x8f\xb7', blank=True)),
                ('product', models.CharField(max_length=500, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('product_name', models.CharField(max_length=500, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0', choices=[(b'ASR1100', b'\xe5\x8d\x8e\xe7\xa1\x95ASR1100'), (b'K880G3', b'\xe8\x8b\xb1\xe4\xb8\x9a\xe8\xbe\xbeK880G3'), (b'ASD2550', b'\xe5\x8d\x8e\xe7\xa1\x95ASD2550'), (b'RS720Q-E8', b'\xe5\x8d\x8e\xe7\xa1\x95RS720Q-E8'), (b'RS300-E9-PS4', b'\xe5\x8d\x8e\xe7\xa1\x95RS300-E9-PS4'), (b'ASR2612', b'\xe5\x8d\x8e\xe7\xa1\x95ASR2612'), (b'D51B-2U', b'\xe5\xb9\xbf\xe8\xbe\xbeD51B-2U'), (b'T41S-2U', b'\xe5\xb9\xbf\xe8\xbe\xbeT41S-2U'), (b'RS300-E9-PS4', b'\xe5\x8d\x8e\xe7\xa1\x95RS300-E9-PS4'), (b'RS520-E8-RS8', b'\xe5\x8d\x8e\xe7\xa1\x95RS520-E8-RS8'), (b'S210-X22RQ', b'\xe5\xb9\xbf\xe8\xbe\xbeS210-X22RQ'), (b'ESC4000G3', b'\xe5\x8d\x8e\xe7\xa1\x95ESC4000G3'), (b'RS520-E8-RS12', b'\xe5\x8d\x8e\xe7\xa1\x95RS520-E8-RS12'), (b'other', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('product_name_other', models.CharField(max_length=500, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('customer_name', models.CharField(max_length=500, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0', choices=[(b'1', b'\xe9\x94\x90\xe6\x8d\xb7'), (b'2', b'\xe6\xb7\xb1\xe4\xbf\xa1\xe6\x9c\x8d'), (b'3', b'\xe4\xb8\x89\xe7\x9b\x9f'), (b'other', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('customer_name_other', models.CharField(max_length=500, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96\xe5\xae\xa2\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('customer', models.CharField(max_length=500, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('exclusion_phase', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe9\x98\xb6\xe6\xae\xb5', choices=[(b'1', b'\xe5\xa4\x84\xe7\x90\x86\xe4\xb8\xad'), (b'2', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')])),
                ('exclusion', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe9\x98\xb6\xe6\xae\xb5', blank=True)),
                ('sn', models.CharField(max_length=250, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81sn')),
                ('enclosure', models.FileField(upload_to=b'', verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6\xe4\xb8\x8a\xe4\xbc\xa0', blank=True)),
                ('phenomenon_description', models.CharField(max_length=500, verbose_name=b'bug\xe7\x8e\xb0\xe8\xb1\xa1\xe8\xaf\xa6\xe7\xbb\x86\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('configuration_information', models.CharField(max_length=500, verbose_name=b'\xe9\x85\x8d\xe7\xbd\xae\xe4\xbf\xa1\xe6\x81\xaf')),
                ('resolvent', models.CharField(max_length=500, verbose_name=b'\xe8\xa7\xa3\xe5\x86\xb3\xe6\x96\xb9\xe6\xb3\x95')),
                ('bug_record', models.TextField(verbose_name=b'BUG\xe8\xae\xb0\xe5\xbd\x95', blank=True)),
                ('submission_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4')),
                ('record_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('time', models.CharField(max_length=250, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('user', models.CharField(max_length=50, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe8\x80\x85', blank=True)),
                ('status', models.BooleanField(default=False)),
                ('number', models.CharField(max_length=50, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7', blank=True)),
            ],
            options={
                'verbose_name': 'fault',
                'verbose_name_plural': 'fae_bugsystem',
            },
        ),
        migrations.AlterModelOptions(
            name='error',
            options={'verbose_name': 'fault', 'verbose_name_plural': 'product_bugsystem'},
        ),
    ]
