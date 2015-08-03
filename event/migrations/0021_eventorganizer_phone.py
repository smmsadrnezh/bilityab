# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0020_auto_20150803_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventorganizer',
            name='phone',
            field=models.IntegerField(default='02188888888'),
        ),
    ]
