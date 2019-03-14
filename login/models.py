# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


def db_init():
            User.objects.all().delete()
            User.objects.create(name='wfj', password='wfj15120413', role=0)
            User.objects.create(name='user1', password='123456', role=1)


class User(models.Model):

            role_choices = [(0, u"管理员"), (1, u"用户")]
            name = models.CharField(verbose_name=u"用户名", max_length=32)
            password = models.CharField(verbose_name=u"密码", max_length=32)
            role = models.IntegerField(verbose_name=u"用户类型", choices=role_choices, default=1)

            def __str__(self):
                  return "%s-%s"%(self.name, self.role)
