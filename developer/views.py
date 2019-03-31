# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import  Query_qes,Question,ResultSimple,Question_mongo,Questions_mongo,Result
from question_web.mymako import render_mako_context,render_mako_tostring_context
from django.shortcuts import render
from django.http import JsonResponse
from bson import ObjectId
import json
from django.http import HttpResponse


import random
# Create your views here.
'''
home为管理者登陆页面
'''


def home(request):
    question_query = Questions_mongo.objects.all()
    return render_mako_context(request, 'question_web/admin_qes_body.html',{
        'config': 'catalog_manage.js'
    })
    # return render_mako_context(request, 'question_web/admin_qes_body.html', {
    #         'question_query': question_query
    # })


'''jqgrid表格获取数据界面'''


def api_catalog_get(request):
    questions = Questions_mongo.objects.all()
    a=[]
    for question in questions:
        item = { "id": str(question.id),"title": question.title, "count": len(question.question),"logo":question.logo, "id": str(question.id),"title": question.title, "count": len(question.question)}
        a.append(item)

    return HttpResponse(json.dumps(a))#, content_type="application/json")


'''jqgrid题目库管理界面'''


def api_catalog_action(request):
    try:
        query_id = request.POST["id"]
        oper = request.POST["oper"]
        if oper == "edit":
            questions = Questions_mongo.objects.get(id=query_id)
            if request.POST.__contains__("title"):
                questions.title = request.POST["title"]
            if request.POST.__contains__("logo"):
                questions.logo = request.POST["logo"]
            questions.save()
            mes = "编辑成功"
        elif oper == "add":
             questions = Questions_mongo()
             questions.title=request.POST["title"]
             questions.result=Result()
             questions.save()
             mes = "添加成功"

        elif oper == "del":
             questions = Questions_mongo.objects.get(id=query_id)
             questions.delete()
             mes = "删除成功"

        return JsonResponse({
            "result": True,
            "message": mes
        })
    except Exception as e:
        return JsonResponse({
            'result':False,
            "messgae":"失败"
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
        url += str(questions.id)+'/'


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


'''admin_qes_edit为显示管理员编辑某题库中 某题view'''


def admin_qes_edit(request, item_id):
    query_id = request.POST["query_id"]
    questions = Questions_mongo.objects.get(id=query_id)
    question = questions.question.get(id=item_id)
    item_html = render_mako_tostring_context(request, '/question_web/qes_item.html',{
        'question':question
    })
    item_content = question.name
    return JsonResponse({
        'result': True,
        'data': item_html,
        'content': item_content,
        'item_id': str(question.id)
    })
'''admin_qes_edit_action为管理员编辑创建某题库中某题行为view'''


def admin_qes_edit_action(request, item_id):
    try:

        query_id = request.POST["query_id"]
        questions = Questions_mongo.objects.get(id=query_id)
        data = request.POST["data"]
        item_data = json.loads(data)
        name = request.POST["name"]
        if  item_id != "none":
            question = questions.question.get(id=item_id)
            question.name = name
            question.items = item_data
            question.save()
            message = "修改成功"
        elif item_id == "none":
            question = Question_mongo()
            question.name = name
            question.items = item_data
            questions.question.append(question)
            questions.save()
            message = "创建成功"
        return JsonResponse({
            'result': True,
            'message': message
        })
    except Exception as e:
        return JsonResponse({
            'result': False,
            'message': "编辑失败"
        })

'''admin_qes_action为编辑某题库view'''


def admin_qes_action(request, query_id):
    question_create = Question_mongo()
    if request.method == 'GET':
        qes_query = Questions_mongo.objects.get(id=query_id)
        questions = qes_query.question
        question_create.items = [{'content': '', 'score': 1}, {'content': '', 'score': 1}]
        question_create.name = qes_query.title
        return render_mako_context(request, '/question_web/admin_qes_action.html', {
            # 'question_name': 1,
            #'question_name': question_mongo.name,
            #'question_items': question_mongo.items,
            'question_default': question_create,
            'query_id': query_id,
            'qes_title': qes_query.title,
            'questions': questions,
        })


'''为管理员编辑某题库结果界面'''


def admin_result_edit(request, query_id):
    if request.method == 'GET':
        try:
            questions = Questions_mongo.objects.get(id=query_id)
            if  len(questions.result.items) == 0:
                result = Result()
                result.items=[{"content": "", "level": "1"}, {"content": "", "level": "1"}, {"content": "", "level": len(questions.question)} ]
                questions.result = result
                questions.save()
            result = questions.result
            return render_mako_context(request, '/question_web/result_edit.html',{
                'result': result,
                'question_name': questions.title,
                'question_id': questions.id,


            })
        except Exception as e:
            return HttpResponse("失败")
    try:
        questions = Questions_mongo.objects.get(id=query_id)
        result = questions.result

        content = request.POST["content"]
        level = request.POST["level"]
        index = int(request.POST["index"])

        if index >= 1:  #编辑结果
            result.items[index-1]["content"] = content
            result.items[index-1]["level"] = level
            result.items.sort(key=lambda k: (int(k.get('level', 0))), reverse= False)
            data = u"编辑成功"
        elif index == -1: #新建结果
            item = {"content": content, "level": level}
            result.items.append(item)
            result.items.sort(key=lambda k: (int(k.get('level', 0))), reverse=False)
            data = u"创建成功"
        questions.save()
        return JsonResponse({
            'result': True,
            'message': data
        })
    except Exception as e:
        return JsonResponse({
            'result':False,
            'message':u"编辑失败"
        })

def admin_result_delete(request, query_id, index):
    try:
        questions = Questions_mongo.objects.get(id=query_id)
        del questions.result.items[int(index)-1]
        questions.result.items.sort(key=lambda k: (int(k.get('level', 0))), reverse=False)
        questions.save()
        return JsonResponse({
            'result': True,
            'message': u"删除成功"
        })
    except Exception as e:
        return JsonResponse({
            'result': False,
            'message': u"删除失败"
        })






