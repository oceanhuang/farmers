# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0003_farmer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('farmers', models.ForeignKey(to='farmers.Farmer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='availability',
            name='farmers',
        ),
        migrations.DeleteModel(
            name='Availability',
        ),
    ]
