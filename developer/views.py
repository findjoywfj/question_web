# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import  Query_qes,Question,ResultSimple,Question_mongo,Questions_mongo,Result
from question_web.mymako import render_mako_context
from django.shortcuts import render
from django.http import JsonResponse
from bson import ObjectId
import json
# Create your views here.
'''
home为管理者登陆页面
'''


def home(request):
    question_query = Questions_mongo.objects.all()

    return render_mako_context(request, 'question_web/admin_qes_body.html', {
            'question_query': question_query
    })
'''
admin_qes_delete为管理员删除题库views
'''
def admin_qes_delete(request, query_id):
    try:
        qes_query = Questions_mongo.objects.get(id=query_id)
        qes_query.delete()
        return JsonResponse({
            'result': True,
            'message': '删除成功'
        })
    except Exception as e:
        return JsonResponse({
            'result': False,
            'message':'删除失败'
        })

'''
admin_qes_delete_item 为管理员删除某题库中某题目view
'''
def admin_qes_delete_item(request,item_id):
    questions = Questions_mongo.objects.get(question__id=item_id)
    question = questions.question.get(id=item_id)

    try:
        index = questions.question.index(question)
        del questions.question[index]
        questions.save()
        url = '/developer/admin/qes_body/action/'
        url+= str(questions.id)+'/'


        return JsonResponse({
            'result': True,
            'message': '删除成功',
            'data': url
        })
    except Exception as e:
        return JsonResponse({
            'result': False,
            'message': '删除失败'
        })


'''admin_qes_edit为管理员编辑某题库中 某题view'''


def admin_qes_edit(request, item_id):
    questions = Questions_mongo.objects.get(question__id=item_id)
    question = questions.question.get(id=item_id)
    if request.method == 'GET':
        return render_mako_context(request, '/question_web/qes_edit.html', {
            'questions':questions,
            'opt': 'edit',
            'question': question
        })
    try:
        data = request.POST["data"]
        name = request.POST["name"]
        item_data = json.loads(data)
        question.name = name
        question.items = item_data
        question.save()
        return JsonResponse({
               'result':True,
               'message': '修改成功'
            })
    except Exception as e:
        return JsonResponse({
            'result': False,
            'message':'修改失败'
        })


'''admin_qes_add为管理员在某题库中 新增加题目view'''


def admin_qes_add(request, query_id):

    questions_mongo = Questions_mongo.objects.get(id=query_id )
    question_mongo = Question_mongo()
    if request.method == 'GET':
        question_mongo.items = [{'content': '', 'score': 1}, {'content': '', 'score': 1}]
        question_mongo.name=questions_mongo.title
        return render_mako_context(request, '/question_web/qes_edit.html', {
            'questions': questions_mongo,
            'question': question_mongo,
            'opt': 'add',
        })
    try:
        data = request.POST["data"]
        name = request.POST["name"]
        item_data = json.loads(data)
        question_mongo.name = name
        question_mongo.items = item_data
        questions_mongo.question.append(question_mongo)
        questions_mongo.save()
        return JsonResponse({
            'result': True,
            'message': '添加成功'
        })
    except Exception as e:
        return JsonResponse({
                  'result' : False,
                    'message' : '添加失败'
                 })



'''admin_qes_action 为管理员编辑某题库view'''


def admin_qes_action(request, query_id):
    qes_query = Questions_mongo.objects.get(id=query_id)
    questions = qes_query.question
    return render_mako_context(request, '/question_web/admin_qes_action.html', {
        # 'question_name': 1,
        'query_id':query_id,
        'qes_title': qes_query.title,
        'questions': questions,


    })


'''admin_query_rename为管理员更改某一题库view'''


def admin_query_rename(request, query_id):
    try:
        query_name = request.POST["rename"]
        query = Questions_mongo.objects.get(id=query_id)
        query.title = query_name
        query.save()
        return JsonResponse({
            'result': True,
            'message': '修改成功'
        })
    except Exception as e:
        return JsonResponse({
            'result': False,
            'message': '修改失败'
        })


'''admin_query_add为管理员增加某题库view'''


def admin_query_add(request):
    try:
        new_name = request.POST["new_name"]
        query = Questions_mongo()
        query.title = new_name
        query.question = []
        query.save()
        return JsonResponse({
            'result':True,
            'message':'测评创建成功'
        })
    except Exception as e:
        return JsonResponse({
            'result':False,
            'message': '测评创建失败'
        })


def admin_result_edit(request, query_id):
    if request.method == 'GET':
        try:
            questions = Questions_mongo.objects.get(id=query_id)
            if  questions.result is None:
                result = Result()
                result.items=[{"content": "", "level": "1"}, {"content": "", "level": "1"}, {"content": "", "level": len(questions.question)} ]
                questions.result = result
                questions.save()
            result = questions.result
            return render_mako_context(request, '/question_web/result_edit.html',{
                'result': result,
                'question_name': questions.title,
                'question_id':questions.id,
            })
        except Exception as e:
            return 0


    try:
        questions = Questions_mongo.objects.get(id=query_id)
        result = questions.result

        data = request.POST["data"]
        data_items = json.loads(data)
        data_items.sort(key=lambda k:(int(k.get('level', 0))), reverse=False)
        result.items=data_items
        questions.save()
        return JsonResponse({
            'result': True,
            'message': u"编辑成功"
        })
    except Exception as e:
        return JsonResponse({
            'result':False,
            'message':u"编辑失败"
        })





