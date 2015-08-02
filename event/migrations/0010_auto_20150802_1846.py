# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0009_auto_20150802_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sport',
            name='event',
            field=models.ForeignKey(related_name='teams', to='event.Event', unique=True),
        ),
    ]
