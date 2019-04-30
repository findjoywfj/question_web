# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from developer.models import Question,Query_qes,ResultSimple,Question_mongo

import mongoengine
# Register your models here.

admin.site.register(Question)
admin.site.register(Query_qes)
admin.site.register(ResultSimple)
#admin.site.register(Question_mongo)
# admin.site.register(Questions_mongo)
# Register your models here.
