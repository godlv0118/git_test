# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import sys
reload(sys)
sys.setdefaultencoding("utf8")
# Create your models here.

class Baidu(models.Model):
    title = models.CharField(max_length=100)      #新闻的标题
    content = models.TextField(max_length=200)    #新闻的大概内容
    from_where = models.CharField(max_length=20,blank=True) #新闻的出处
    url = models.CharField(max_length=100)        #新闻的链接

    def __str__(self):
        return self.title