# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from developer.models import Question,Query_qes,ResultSimple
from question_web.mymako import render_mako_context
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    qes_query = Query_qes.objects.all()
    return render_mako_context(request, '/question_web/home.html',
                               {'qes_query': qes_query})

def qes_show(request, query_id):

    qes_query = Query_qes.objects.get(id=query_id)
    questions = Question.objects.all().filter(belong_id=query_id)
    return render_mako_context(request, '/question_web/qes_body.html', {
        #'question_name': 1,
        'qes_title':qes_query.name,
        'questions': questions,
        'num': questions.count()


    })

def qes_result(request,query_id, score):
    try:
        result = ResultSimple.objects.get(belong_id = query_id)
        score_temp =  int(score)
        if score_temp <= result.level_1:
            content = result.content_1
        elif score_temp > result.level_1 and score_temp <= result.level_2:
            content = result.content_2
        else:
            content = result.content_3
        return render_mako_context(request, 'question_web/qes_result.html',{
                'name': Query_qes.objects.get(id=query_id).name,
                'result': content,
                'belong': query_id,
            })
        # return JsonResponse({
        #         'result': True,
        #         'data': content
        # })
    except Exception as e:
        return JsonResponse({
            'result': False,
            'message': u'评分失败'
        })
