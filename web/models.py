# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from djnago.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    text = models.CharField(man_lengh=255)
    date = models.DateTimeField()
    amout = models.BigIntergerField()
    user = models.ForeignKey(User) 
