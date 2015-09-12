# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Graffiti',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('photo', models.ImageField(upload_to='')),
                ('lat', models.FloatField(default=49.2630182016568)),
                ('lon', models.FloatField(default=-123.120131523468)),
                ('count', models.IntegerField(default=0)),
                ('comment', models.ForeignKey(to='graffiki_app.Comment', related_name='graffitis')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('image', models.FileField(upload_to='profile/%Y/%m/%d')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='graffiti',
            field=models.ForeignKey(to='graffiki_app.Graffiti', related_name='comments'),
        ),
    ]
