# -*- coding: utf-8 -*-
from __future__ import unicode_literals



# Create your models here.
# -*- coding: utf-8 -*-

from django.db import models

quit


# Create your models here.
def db_init():
    Question.objects.all().delete()
    Query_qes.objects.all().delete()
    ResultSimple.objects.all().delete()
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

    ResultSimple.objects.create(
        belong_id=query_1.id,
        level_1=6,
        level_2=14,
        content_1=u"你没有精神分裂的倾向，继续保持吧",
        content_2=u"你认为自己的行为、感觉像是得了精神分裂症，实际上这只是所有人都会经历的一段过程罢了，可能是情绪积压，可能是一时冲动，过段时间就会不药而愈了，不用过分担心。",
        content_3=u"你有一定的精神分裂倾向，你的情感比较淡薄，无论是对亲人或是所谓的朋友；"
                  u"你有些自卑，比起热闹，你更希望独处、不愿暴露自己；你时常会认为自己与这个社会格格不入，没人了解你。"

    )
    ResultSimple.objects.create(
        belong_id=query_2.id,
        level_1=6,
        level_2=15,
        content_1=u"你与反社会人格相距甚远 你愿意让人觉得温暖，强调社会责任感，善良， 凭良心做事，道德感更高。",
        content_2=u"像狼人一样，你在某些时候会表现出“反社会人格” 虽然，平时看起来也是个“谦谦君子”，不过你也有放荡不羁，无恶不欢的一面。",
        content_3=u"你，就是你了！ 你的柔软被狼吃掉了，是强硬派中的强硬派，可以面不改色心不掉地“违法乱纪，胡作非为”！"

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


class ResultSimple(models.Model):
     belong = models.ForeignKey(verbose_name=u"所属题库", to=Query_qes)
     level_1 = models.IntegerField(verbose_name=u"分割线1")
     level_2 = models.IntegerField(verbose_name=u"分割线2")
     content_1 = models.TextField(verbose_name=u"第一级结果")
     content_2 = models.TextField(verbose_name=u"第二级结果")
     content_3 = models.TextField(verbose_name=u"第三级结果")

     def __str__(self):
         return "%s" % (self.belong_id)