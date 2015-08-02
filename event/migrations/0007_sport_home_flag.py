# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20150802_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='home_flag',
            field=models.ImageField(upload_to='', null=True),
        ),
    ]
