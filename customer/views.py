# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from developer.models import Question,Query_qes,ResultSimple,Questions_mongo,Question_mongo
from question_web.mymako import render_mako_context
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    qes_query = Questions_mongo.objects.all()
    return render_mako_context(request, '/question_web/home.html',
                               {'qes_query': qes_query})

def qes_show(request, query_id):

    qes_query = Questions_mongo.objects.get(id=query_id)
    questions = qes_query.question
    num = len(questions)
    return render_mako_context(request, '/question_web/qes_body.html', {
        #'question_name': 1,
        'qes_title':qes_query.title,
        'questions': questions,
        'num': num


    })

def qes_result(request,query_id, score):
    try:
        questions = Questions_mongo.objects.get(id=query_id)
        result = questions.result
        score_temp = int(score)
        result_data = result.items
        content = "未查到结果"
        for item in result_data:
            if score_temp <= int(item["level"]):
                content = item["content"]
                break

        return render_mako_context(request, 'question_web/qes_result.html',{
                'title': questions.title,
                'result': content,
                'query_id': query_id,
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
