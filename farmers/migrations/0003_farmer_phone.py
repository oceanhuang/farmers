# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0002_auto_20150130_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='phone',
            field=models.IntegerField(default=11111111111, max_length=10),
            preserve_default=True,
        ),
    ]
