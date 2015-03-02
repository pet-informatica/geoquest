# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='exam',
            field=models.CharField(verbose_name='Prova', default='', max_length=100),
            preserve_default=False,
        ),
    ]
