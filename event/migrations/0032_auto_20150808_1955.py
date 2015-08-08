# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0031_auto_20150808_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='capacity',
        ),
        migrations.AddField(
            model_name='showtime',
            name='capacity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
