# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import  Query_qes,Question,ResultSimple
from question_web.mymako import render_mako_context
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
'''
home为管理者登陆页面
'''


def home(request):
    qes_query = Query_qes.objects.all()

    return render_mako_context(request, 'question_web/admin_qes_body.html', {
            'qes_query': qes_query
    })
'''
admin_qes_delete为管理员删除题库views
'''
def admin_qes_delete(request, query_id):
    try:
        qes_query = Query_qes.objects.get(id=query_id)
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
    try:
        question = Question.objects.all().get(id=item_id)
        query_id = question.belong_id
        question.delete()
        query = Query_qes.objects.get(id=query_id)
        query.count= Question.objects.all().filter(belong_id=query_id).count()
        query.save()
        url = '/developer/admin/qes_body/action/'
        url+= str(query_id)+'/'


        return JsonResponse({
            'result': True,
            'message': '删除成功',
            'data': url
        })
    except Exception as e:
        return JsonResponse({
            'result': True,
            'message': '删除失败'
        })


'''admin_qes_edit为管理员编辑某题库中 某题view'''


def admin_qes_edit(request, item_id):
    question = Question.objects.get(id=item_id)
    query_id = question.belong_id
    query = Query_qes.objects.get(id=query_id)
    if request.method == 'GET':

        return render_mako_context(request, '/question_web/qes_edit.html', {
            'query':query,
            'opt': 'edit',
            'question': question
        })
    try:
       question.name = request.POST["qes_name"]
       question.item_1 = request.POST["item_1"]
       question.item_2 = request.POST["item_2"]
       question.item_1_score = request.POST["item_1_score"]
       question.item_2_score = request.POST["item_2_score"]
       question.save()
       return JsonResponse({
           'result':True,
           'message': '修改成功'
       })
    except Exception as e:
        return JsonResponse({
            'result':False,
            'message':'修改失败'
        })


'''admin_qes_add为管理员在某题库中 新增加题目view'''


def admin_qes_add(request, query_id):
    question = Question()
    if request.method == 'GET':

        question.name = "新增题目"
        question.item_1 = ""
        question.item_2 = ""
        question.item_1_score = 1
        question.item_2_score = 1
        question.belong_id = query_id
        query = Query_qes.objects.get(id=query_id)
        return render_mako_context(request, '/question_web/qes_edit.html', {
            'query': query,
            'opt': 'add',
            'question': question

        })

    try:

        question.name = request.POST["qes_name"]
        question.item_1 = request.POST["item_1"]
        question.item_2 = request.POST["item_2"]
        question.item_1_score = request.POST["item_1_score"]
        question.item_2_score = request.POST["item_2_score"]
        question.belong_id = query_id
        count = Question.objects.all().filter(belong_id=query_id).count()
        question.order=count+1
        question.save()
        query = Query_qes.objects.get(id=query_id)
        query.count=count+1
        query.save()
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
    qes_query = Query_qes.objects.get(id=query_id)
    questions = Question.objects.all().filter(belong_id=query_id)
    return render_mako_context(request, '/question_web/admin_qes_action.html', {
        # 'question_name': 1,
        'query_id':query_id,
        'qes_title': qes_query.name,
        'questions': questions,


    })


'''admin_query_rename为管理员更改某一题库view'''


def admin_query_rename(request, query_id):
    try:
        query_name = request.POST["rename"]
        query = Query_qes.objects.get(id=query_id)
        query.name = query_name
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
        query = Query_qes()
        query.name = new_name
        query.count = 0
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
            result = ResultSimple.objects.get(belong_id=query_id)
            return render_mako_context(request, '/question_web/result_edit.html',{
                'result': result
            })
        except ResultSimple.DoesNotExist:
            result=ResultSimple.objects.create(content_1="",content_2="",content_3="",level_1=1,level_2=10,belong_id=query_id)
            return render_mako_context(request,'/question_web/result_edit.html',{
                'result':result
            })

    try:
        result = ResultSimple.objects.get(belong_id=query_id)
        result.content_1 = request.POST["content_1"]
        result.content_2 = request.POST["content_2"]
        result.content_3 = request.POST["content_3"]
        result.level_1 = request.POST["level_1"]
        result.level_2 = request.POST["level_2"]
        result.save()
        return JsonResponse({
            'result':True,
            'message':u"编辑成功"
        })
    except Exception as e:
        return JsonResponse({
            'result':False,
            'message':u"编辑失败"
        })





