# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0030_auto_20150806_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='photo',
            new_name='landscape',
        ),
        migrations.AddField(
            model_name='event',
            name='portrait',
            field=models.ImageField(default='default.jpg', null=True, upload_to=''),
        ),
    ]
