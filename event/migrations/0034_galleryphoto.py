# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0033_auto_20150809_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pic', models.ImageField(upload_to='')),
                ('event', models.ForeignKey(to='event.Event', related_name='gallery_photos')),
            ],
        ),
    ]
