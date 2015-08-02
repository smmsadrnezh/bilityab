# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr',
                 models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False, parent_link=True,
                                      auto_created=True)),
                ('registration_date', models.DateField()),
                ('balance', models.FloatField()),
                ('is_organizer', models.BooleanField(default=0)),
                ('gender', models.BooleanField(default=0)),
                ('phone', models.IntegerField(default='02188888888')),
                ('test', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
