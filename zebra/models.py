# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Page(models.Model):
    page_title= models.CharField(max_length=1000)
    page_title_2= models.CharField(max_length=100)
    page_content= models.CharField(max_length=1000)
