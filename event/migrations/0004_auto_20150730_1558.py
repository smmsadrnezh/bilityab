# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0003_auto_20150730_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='parent',
        ),
        migrations.AddField(
            model_name='categories',
            name='parent',
            field=models.ManyToManyField(to='event.Categories', null=True),
        ),
    ]