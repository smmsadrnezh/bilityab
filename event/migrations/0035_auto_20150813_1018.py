# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0034_galleryphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='musicians',
            field=models.CharField(max_length=1000),
        ),
    ]
