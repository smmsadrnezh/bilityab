# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_auto_20150803_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
