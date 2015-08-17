# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20150817_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.DateTimeField(),
        ),
    ]
