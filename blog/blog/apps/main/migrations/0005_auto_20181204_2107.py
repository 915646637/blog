# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-04 13:07
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181204_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文'),
        ),
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