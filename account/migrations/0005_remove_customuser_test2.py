# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150802_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='test2',
        ),
    ]
