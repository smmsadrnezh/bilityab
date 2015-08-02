# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(default=b'02188888888'),
        ),
    ]