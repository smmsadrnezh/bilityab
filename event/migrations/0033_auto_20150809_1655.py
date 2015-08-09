# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0032_auto_20150808_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positionprice',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
