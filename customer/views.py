# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from developer.models import Question,Query_qes,ResultSimple,Questions_mongo,Question_mongo
from question_web.mymako import render_mako_context
from django.http import JsonResponse
from mongoengine.errors import DoesNotExist
from customer.models import Record
from django.shortcuts import render
import datetime
import json
from django.http import HttpResponse
# Create your views here.

def home(request):
    questions = Questions_mongo.objects.all()
    return render_mako_context(request, '/question_web/home.html',
                             {'questions': questions})


def qes_show(request, query_id, user_type):

    qes_query = Questions_mongo.objects.get(id=query_id)
    questions = qes_query.question
    num = len(questions)
    return render_mako_context(request, '/question_web/qes_body.html', {
        #'question_name': 1,
        'qes_title':qes_query.title,
        'questions': questions,
        'num': num,
        'user_type':user_type



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
        #将结果存入数据库
        username = request.session["name"]
        datenow = datetime.datetime.now()
        try:
            record = Record.objects.get(belong=username)
            record.desprition.append({"found_time": datenow, "score": score_temp,
                                      "content": content, "questions_name": questions.title, "questions_id": query_id})
            record.save()
        except DoesNotExist:
            record = Record(belong=username)
            record.desprition.append({"found_time": datenow, "score": score_temp,
                                      "content": content,"questions_name": questions.title, "questions_id": query_id})
            record.save()
        except Exception as e:
            return JsonResponse({
                'result': False,
                'message': '存储失败'
            })



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
def record_show(request):
    return render_mako_context(request, 'question_web/record.html', {
        'config': 'record_manage.js',
    })
def api_record_get(request):
    user_name = request.session["name"]
    a = []
    try:
       user = Record.objects.get(belong=user_name)
       for item in user.desprition:
           data = {"questions_name": item["questions_name"], "score": item["score"], "content": item["content"],
                   "found_time": item["found_time"].strftime('%Y-%m-%d %H:%M:%S')}
           a.append(data)
       return HttpResponse(json.dumps(a))
    except DoesNotExist:
        return HttpResponse(json.dumps(a))
    except Exception as e:
        return HttpResponse(json.dumps(a))

