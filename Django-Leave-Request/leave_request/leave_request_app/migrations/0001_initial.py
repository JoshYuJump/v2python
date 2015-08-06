# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('req_user', models.CharField(max_length=100, verbose_name='\u8bf7\u5047\u4eba')),
                ('req_depart', models.CharField(max_length=200, verbose_name='\u90e8\u95e8')),
                ('req_duty', models.CharField(max_length=200, verbose_name='\u804c\u52a1')),
                ('req_type', models.CharField(max_length=200, verbose_name='\u8bf7\u5047\u7c7b\u578b')),
                ('req_begin', models.DateTimeField(verbose_name='\u8bf7\u5047\u5f00\u59cb\u65f6\u95f4')),
                ('req_end', models.DateTimeField(verbose_name='\u8bf7\u5047\u7ed3\u675f\u65f6\u95f4')),
                ('req_reason', models.CharField(max_length=500, verbose_name='\u8bf7\u5047\u4e8b\u7531')),
                ('req_contact', models.CharField(max_length=200, verbose_name='\u8bf7\u5047\u671f\u95f4\u8054\u7cfb\u65b9\u5f0f')),
                ('req_client', models.CharField(max_length=200, verbose_name='\u8bf7\u5047\u671f\u95f4\u5de5\u4f5c\u59d4\u6258\u4eba')),
            ],
        ),
    ]
