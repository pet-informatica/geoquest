# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.CharField(max_length=200, verbose_name='Descricao')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('question', models.TextField(verbose_name='Pergunta')),
                ('option_a', models.CharField(max_length=500, verbose_name='Letra A')),
                ('option_b', models.CharField(max_length=500, verbose_name='Letra B')),
                ('option_c', models.CharField(max_length=500, verbose_name='Letra C')),
                ('option_d', models.CharField(max_length=500, verbose_name='Letra D')),
                ('option_e', models.CharField(max_length=500, verbose_name='Letra E')),
                ('answer', models.CharField(max_length=1, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E')])),
                ('category', models.ForeignKey(to='questions.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
