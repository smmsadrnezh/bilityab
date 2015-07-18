# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilityab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concert',
            name='id',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='id',
        ),
        migrations.AlterField(
            model_name='concert',
            name='event',
            field=models.OneToOneField(primary_key=True, serialize=False, to='bilityab.Event'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='event',
            field=models.OneToOneField(primary_key=True, serialize=False, to='bilityab.Event'),
        ),
        migrations.AlterField(
            model_name='sport',
            name='event',
            field=models.OneToOneField(primary_key=True, serialize=False, to='bilityab.Event'),
        ),
    ]
