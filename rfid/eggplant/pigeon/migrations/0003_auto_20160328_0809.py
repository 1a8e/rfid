# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-28 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pigeon', '0002_auto_20160327_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scroll',
            name='pubDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='scroll',
            name='scrollFrom',
            field=models.CharField(max_length=80, verbose_name='from'),
        ),
        migrations.AlterField(
            model_name='scroll',
            name='scrollID',
            field=models.CharField(max_length=40, verbose_name='RFID'),
        ),
        migrations.AlterField(
            model_name='scroll',
            name='scrollMessage',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='scroll',
            name='scrollTo',
            field=models.CharField(max_length=80, verbose_name='to'),
        ),
    ]