# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('zip_prefix', models.CharField(max_length=2)),
            ],
        ),
    ]
