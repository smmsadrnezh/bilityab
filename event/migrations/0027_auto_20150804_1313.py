# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0026_auto_20150804_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventrating',
            name='rate',
            field=models.FloatField(),
        ),
    ]
