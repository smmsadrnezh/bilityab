# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0002_auto_20150720_1809'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(default='02188888888'),
        ),
    ]
