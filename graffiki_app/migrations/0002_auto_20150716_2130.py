# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graffiki_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graffiti',
            name='comment',
        ),
        migrations.AddField(
            model_name='graffiti',
            name='description',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='graffiti',
            name='photo',
            field=models.ImageField(upload_to='graffitiPics'),
        ),
    ]
