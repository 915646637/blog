# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-04 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181203_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(default='/static/img/article/default.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='img',
            field=models.ImageField(default='/static/img/carousel/default.jpg', max_length=200, upload_to='', verbose_name='轮播图片'),
        ),
    ]
