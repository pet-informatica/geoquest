# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_badge'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('about_me', models.TextField(null=True, blank=True)),
                ('facebook_id', models.BigIntegerField(null=True, blank=True, unique=True)),
                ('access_token', models.TextField(help_text='Facebook token for offline access', null=True, blank=True)),
                ('facebook_name', models.CharField(null=True, max_length=255, blank=True)),
                ('facebook_profile_url', models.TextField(null=True, blank=True)),
                ('website_url', models.TextField(null=True, blank=True)),
                ('blog_url', models.TextField(null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], null=True, max_length=1, blank=True)),
                ('raw_data', models.TextField(null=True, blank=True)),
                ('facebook_open_graph', models.NullBooleanField(help_text='Determines if this user want to share via open graph')),
                ('new_token_required', models.BooleanField(help_text='Set to true if the access token is outdated or lacks permissions', default=False)),
                ('image', models.ImageField(upload_to='images\\facebook_profiles/%Y/%m/%d', null=True, max_length=255, blank=True)),
                ('badges', models.ManyToManyField(to='questions.Badge')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
