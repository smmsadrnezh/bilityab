# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ticket', '0006_auto_20150807_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketposition',
            name='section',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
