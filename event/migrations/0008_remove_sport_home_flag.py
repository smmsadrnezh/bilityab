# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0007_sport_home_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='home_flag',
        ),
    ]
