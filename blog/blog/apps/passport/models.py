from django.db import models

# Create your models here.

# coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    img = models.CharField(max_length=200, default='/static/tx/default.jpg', verbose_name='头像地址')
    intro = models.CharField(max_length=200, blank=True, null=True, verbose_name='简介')

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name