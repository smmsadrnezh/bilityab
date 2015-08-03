# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0022_auto_20150803_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventorganizer',
            name='photo',
            field=models.ImageField(upload_to='', null=True),
        ),
    ]
