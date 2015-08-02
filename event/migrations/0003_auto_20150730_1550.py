# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_positionprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('parent', models.ForeignKey(to='event.Categories', null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'رویداد', 'verbose_name_plural': 'رویدادها'},
        ),
        migrations.AlterModelOptions(
            name='positionprice',
            options={'verbose_name_plural': 'قیمت ها'},
        ),
        migrations.RemoveField(
            model_name='event',
            name='price',
        ),
        migrations.RemoveField(
            model_name='event',
            name='type',
        ),
        migrations.AddField(
            model_name='positionprice',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(to='event.Categories', related_name='events'),
        ),
    ]
