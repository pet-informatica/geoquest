# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_badge'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Nivel', max_length=1, choices=[(1, '1'), (2, '2'), (3, '3')]),
            preserve_default=False,
        ),
    ]
