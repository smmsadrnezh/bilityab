# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0036_auto_20150817_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='landscape',
            field=models.ImageField(null=True, upload_to='/media/', default='default.jpg'),
        ),
        migrations.AlterField(
            model_name='event',
            name='portrait',
            field=models.ImageField(null=True, upload_to='/media/', default='default.jpg'),
        ),
    ]
