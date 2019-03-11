# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

from django.db import models

quit


# Create your models here.
def db_init():
    Question.objects.all().delete()
    Query_qes.objects.all().delete()
    Query_qes.objects.create(name=u"测你是否有精神分裂",count=10)
    Query_qes.objects.create(name=u"反社会人格测试",count=10)
    qes_choices = [u"我喜欢到我从来没有去过的地方游览",
                   u"我曾一连几天，几个星期，几个月什么也不想干，因为总是提不起精神",
                   u"有时我有一种强烈的冲动，去做一些惊人或有害的事",
                   u"我的记忆力似乎不错",
                   u"遇到同学或不常见朋友。除非他们先向我打招呼，不然我就装作没看见",
                   u"做什么事情，我都感到难以开头",
                   u"我的日常生活中，充满着使我感兴趣的事情",
                   u"我曾经有过几次突然不能控制自己的行动或言语，但当时我的头脑还很清醒。",
                   u"我拒绝玩那些我玩不好的游戏",
                   u"我不喜欢有人在我身旁"]
    qes_choices_1=[u"我干什么很少提前做计划，我属于那种一时兴起想干什么就干什么的人",
                   u"只要不被发现，欺骗伴侣其实也没什么",
                   u"如果临时出现更好的机会，取消以前和人达成的誓约也没有什么",
                   u"看见受伤的小动物在痛苦中挣扎，我一点触动都没有",
                   u"我特别喜欢飙车，坐云霄飞车，蹦极等高刺激活动",
                   u"我为达目的不择手段，即使损害别人，利用别人也在所不惜",
                   u"我特别有说服力。天生就能指使别人替我办事",
                   u"我能胜任危险性高的工作，因为我脑子特别灵敏",
                   u"当别人在巨大压力下惶惶不安时，我还能镇定自若",
                   u"我之所以能欺诈某人，是因为他们容易被欺诈，这是他们自己的问题"]
    query_1 =Query_qes.objects.get(name=u"测你是否有精神分裂")
    query_2 = Query_qes.objects.get(name=u"反社会人格测试")
    for item in range(1, 11, 1):
        Question.objects.create(
            name=qes_choices[item-1],
            item_1=u"是",
            item_2=u"不是",
            item_1_score=1,
            item_2_score=0,
            belong_id=query_1.id
        )

    for item in range(1, 11, 1):
        Question.objects.create(
            name=qes_choices_1[item-1],
            item_1=u"是",
            item_2=u"不是",
            item_1_score=1,
            item_2_score=0,
            belong_id=query_2.id
        )


class Query_qes(models.Model):
    name = models.TextField(verbose_name=u"测评名称")
    count = models.IntegerField(verbose_name=u"题目数量",default=0)
    def __str__(self):
        return "%s=%s" %(self.name, self.id)
class Question(models.Model):
    name = models.TextField(verbose_name=u"题目名称")
    item_1 = models.TextField(verbose_name=u"条目一")
    item_2 = models.TextField(verbose_name=u"条目二")
    belong = models.ForeignKey(verbose_name=u"所属题库", to=Query_qes)
    item_1_score = models.IntegerField(verbose_name=u"得分1")
    item_2_score = models.IntegerField(verbose_name=u"得分2")

    def __str__(self):
        return "%s-%s" % (self.name, self.belong_id)