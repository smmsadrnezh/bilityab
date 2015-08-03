# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_customuser_test2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='registration_date',
            new_name='birth_date',
        ),
    ]
