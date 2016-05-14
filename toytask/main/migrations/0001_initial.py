# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('image', models.FileField(verbose_name='Select an Image', upload_to='photos')),
                ('ques', models.CharField(max_length=30, verbose_name='Question?')),
            ],
        ),
    ]
