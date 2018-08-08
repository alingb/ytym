# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0010_auto_20170809_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='error',
            name='record_update',
            field=models.TextField(max_length=500, verbose_name=b'\xe8\xae\xb0\xe5\xbd\x95\xe6\x9b\xb4\xe6\x96\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='bug_describe',
            field=models.CharField(max_length=500, verbose_name=b'BUG\xe7\xae\x80\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='error',
            name='bug_level',
            field=models.CharField(max_length=500, verbose_name=b'BUG\xe7\xad\x89\xe7\xba\xa7', choices=[(b'1', b'\xe4\xb8\x80\xe8\x88\xac'), (b'2', b'\xe4\xb8\xa5\xe9\x87\x8d'), (b'3', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe4\xb8\xa5\xe9\x87\x8d')]),
        ),
        migrations.AlterField(
            model_name='error',
            name='bug_person',
            field=models.CharField(max_length=500, verbose_name=b'BUG\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba'),
        ),
        migrations.AlterField(
            model_name='error',
            name='bug_record',
            field=models.TextField(max_length=500, verbose_name=b'BUG\xe8\xae\xb0\xe5\xbd\x95', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='configuration_information',
            field=models.CharField(max_length=500, verbose_name=b'\xe9\x85\x8d\xe7\xbd\xae\xe4\xbf\xa1\xe6\x81\xaf'),
        ),
        migrations.AlterField(
            model_name='error',
            name='customer',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='customer_name',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0', choices=[(b'1', b'\xe9\x94\x90\xe6\x8d\xb7'), (b'2', b'\xe6\xb7\xb1\xe4\xbf\xa1\xe6\x9c\x8d'), (b'3', b'\xe4\xb8\x89\xe7\x9b\x9f'), (b'other', b'\xe5\x85\xb6\xe4\xbb\x96')]),
        ),
        migrations.AlterField(
            model_name='error',
            name='customer_name_other',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96\xe5\xae\xa2\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='discovery',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\x8f\x91\xe7\x8e\xb0\xe9\x80\x94\xe5\xbe\x84', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='discovery_phase',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\x8f\x91\xe7\x8e\xb0\xe9\x80\x94\xe5\xbe\x84', choices=[(b'1', b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x86\x85\xe9\x83\xa8'), (b'2', b'\xe5\xae\xa2\xe6\x88\xb7'), (b'other', b'\xe5\x85\xb6\xe4\xbb\x96')]),
        ),
        migrations.AlterField(
            model_name='error',
            name='discovery_phase_other',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96\xe5\x8f\x91\xe7\x8e\xb0\xe9\x80\x94\xe5\xbe\x84', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='email',
            field=models.CharField(max_length=500, verbose_name=b'\xe6\x8a\x84\xe9\x80\x81\xe4\xba\xba\xe5\x91\x98', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='exclusion_phase',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe9\x98\xb6\xe6\xae\xb5', choices=[(b'1', b'\xe5\xa4\x84\xe7\x90\x86\xe4\xb8\xad'), (b'2', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')]),
        ),
        migrations.AlterField(
            model_name='error',
            name='phenomenon_description',
            field=models.CharField(max_length=500, verbose_name=b'bug\xe7\x8e\xb0\xe8\xb1\xa1\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='error',
            name='product',
            field=models.CharField(max_length=500, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='product_name',
            field=models.CharField(max_length=500, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0', choices=[(b'ASR1100', b'\xe5\x8d\x8e\xe7\xa1\x95ASR1100'), (b'K880G3', b'\xe8\x8b\xb1\xe4\xb8\x9a\xe8\xbe\xbeK880G3'), (b'ASD2550', b'\xe5\x8d\x8e\xe7\xa1\x95ASD2550'), (b'RS720Q-E8', b'\xe5\x8d\x8e\xe7\xa1\x95RS720Q-E8'), (b'RS300-E9-PS4', b'\xe5\x8d\x8e\xe7\xa1\x95RS300-E9-PS4'), (b'ASR2612', b'\xe5\x8d\x8e\xe7\xa1\x95ASR2612'), (b'D51B-2U', b'\xe5\xb9\xbf\xe8\xbe\xbeD51B-2U'), (b'T41S-2U', b'\xe5\xb9\xbf\xe8\xbe\xbeT41S-2U'), (b'RS300-E9-PS4', b'\xe5\x8d\x8e\xe7\xa1\x95RS300-E9-PS4'), (b'RS520-E8-RS8', b'\xe5\x8d\x8e\xe7\xa1\x95RS520-E8-RS8'), (b'S210-X22RQ', b'\xe5\xb9\xbf\xe8\xbe\xbeS210-X22RQ'), (b'ESC4000G3', b'\xe5\x8d\x8e\xe7\xa1\x95ESC4000G3'), (b'RS520-E8-RS12', b'\xe5\x8d\x8e\xe7\xa1\x95RS520-E8-RS12'), (b'other', b'\xe5\x85\xb6\xe4\xbb\x96')]),
        ),
        migrations.AlterField(
            model_name='error',
            name='product_name_other',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='project',
            field=models.CharField(max_length=500, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='project_name',
            field=models.CharField(max_length=500, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0', choices=[(b'ELOG', b'\xe9\x94\x90\xe6\x8d\xb7ELOG'), (b'RG-RCP', b'\xe9\x94\x90\xe6\x8d\xb7RG-RCP'), (b'RCD6000-Office', b'\xe9\x94\x90\xe6\x8d\xb7RCD6000-Office'), (b'RCD6000-Main', b'\xe9\x94\x90\xe6\x8d\xb7RCD6000-Main'), (b'RG-SE04', b'\xe9\x94\x90\xe6\x8d\xb7RG-SE04'), (b'RG-ONC-AIO-CTL', b'\xe9\x94\x90\xe6\x8d\xb7RG-ONC-AIO-CTL'), (b'RG-RCM1000-Office', b'\xe9\x94\x90\xe6\x8d\xb7RG-RCM1000-Office'), (b'RG-RCM1000-Edu', b'\xe9\x94\x90\xe6\x8d\xb7RG-RCM1000-Edu'), (b'RG-RCM1000-Smart', b'\xe9\x94\x90\xe6\x8d\xb7RG-RCM1000-Smart'), (b'MDBE', b'\xe7\xbe\x8e\xe7\x94\xb5\xe8\xb4\x9d\xe5\xb0\x94'), (b'ZJCC', b'\xe5\xb9\xbf\xe4\xb8\x9c\xe7\xb4\xab\xe6\x99\xb6\xe5\xad\x98\xe5\x82\xa8'), (b'UDS1022-G', b'\xe9\x94\x90\xe6\x8d\xb7UDS1022-G'), (b'UDS1022-G1', b'\xe9\x94\x90\xe6\x8d\xb7UDS1022-G1'), (b'UDS2000-C', b'\xe9\x94\x90\xe6\x8d\xb7UDS2000-C'), (b'UDS2000-E', b'\xe9\x94\x90\xe6\x8d\xb7UDS2000-E'), (b'UDS2000-E1', b'\xe9\x94\x90\xe6\x8d\xb7UDS2000-E1'), (b'RG-CES', b'\xe9\x94\x90\xe6\x8d\xb7RG-CES'), (b'RG-CPV-M', b'\xe9\x94\x90\xe6\x8d\xb7RG-CPV-M'), (b'RG-CPV-S', b'\xe9\x94\x90\xe6\x8d\xb7RG-CPV-S'), (b'2513(M1)', b'\xe4\xb8\x89\xe7\x9b\x9f2513(M1)'), (b'2513(M3)', b'\xe4\xb8\x89\xe7\x9b\x9f2513(M3)'), (b'2513(VM3)', b'\xe4\xb8\x89\xe7\x9b\x9f2513(VM3)'), (b'ASERVER-2400', b'\xe6\xb7\xb1\xe4\xbf\xa1\xe6\x9c\x8dASERVER-2400'), (b'ASERVER-2405', b'\xe6\xb7\xb1\xe4\xbf\xa1\xe6\x9c\x8dASERVER-2405'), (b'VDS-5050', b'\xe6\xb7\xb1\xe4\xbf\xa1\xe6\x9c\x8dVDS-5050'), (b'VDS-6550', b'\xe6\xb7\xb1\xe4\xbf\xa1\xe6\x9c\x8dVDS-6550'), (b'VDS-8050', b'\xe6\xb7\xb1\xe4\xbf\xa1\xe6\x9c\x8dVDS-8050'), (b'VDS-G680', b'\xe6\xb7\xb1\xe4\xbf\xa1\xe6\x9c\x8dVDS-G680'), (b'other', b'\xe5\x85\xb6\xe4\xbb\x96')]),
        ),
        migrations.AlterField(
            model_name='error',
            name='project_name_other',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='software_name',
            field=models.CharField(max_length=500, verbose_name=b'\xe6\xb5\x8b\xe8\xaf\x95\xe8\xbd\xaf\xe4\xbb\xb6\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='software_version',
            field=models.CharField(max_length=500, verbose_name=b'\xe8\xbd\xaf\xe4\xbb\xb6\xe7\x89\x88\xe6\x9c\xac', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='step_description',
            field=models.CharField(max_length=500, verbose_name=b'bug\xe4\xba\xa7\xe7\x94\x9f\xe6\xad\xa5\xe9\xaa\xa4\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='error',
            name='suggested_view',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xbb\xba\xe8\xae\xae\xe7\x9c\x8b\xe6\xb3\x95'),
        ),
        migrations.AlterField(
            model_name='error',
            name='test_model',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x84\xe7\x90\x86\xe6\x96\xb9\xe5\xbc\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='test_person',
            field=models.CharField(max_length=500, verbose_name=b'\xe6\xb5\x8b\xe8\xaf\x95\xe4\xba\xba\xe5\x91\x98', blank=True),
        ),
        migrations.AlterField(
            model_name='error',
            name='test_site',
            field=models.CharField(max_length=500, verbose_name=b'\xe6\xb5\x8b\xe8\xaf\x95\xe5\x9c\xb0\xe7\x82\xb9', blank=True),
        ),
    ]
