# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Farmers',
            new_name='Farmer',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RemoveField(
            model_name='availabilities',
            name='farmers',
        ),
        migrations.DeleteModel(
            name='Availabilities',
        ),
        migrations.AddField(
            model_name='availability',
            name='farmers',
            field=models.ForeignKey(to='farmers.Farmer'),
            preserve_default=True,
        ),
    ]
