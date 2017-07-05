# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20,null=False,unique=True)
    password = models.CharField(max_length=20,null=False)
    name = models.CharField(max_length=10,null=False,unique=True) #名称


class Blog(models.Model):
    title = models.CharField(max_length=50,null=False)
    body = models.TextField()
    owner = models.ForeignKey(User) #博客的创建者

    def __str__(self):
        return self.title