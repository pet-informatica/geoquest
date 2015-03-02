# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20150225_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.CharField(max_length=200, verbose_name='Descricao')),
                ('category', models.ForeignKey(to='questions.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
