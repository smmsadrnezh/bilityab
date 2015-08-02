# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20150730_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='test',
            new_name='test2',
        ),
    ]
