# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import mongoengine
from django.db import models

# Create your models here.


class Record(mongoengine.DynamicDocument):
    belong = mongoengine.StringField(max_length=20, required=True)
    desprition = mongoengine.ListField(default=[])
