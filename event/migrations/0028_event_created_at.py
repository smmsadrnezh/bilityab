# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0027_auto_20150804_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
