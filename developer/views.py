# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import  Query_qes,Question
from question_web.mymako import render_mako_context
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    qes_query = Query_qes.objects.all()
    # return render_mako_context(request, 'question_web/test.html',{
    #     'question': '123'
    # })
    return render_mako_context(request, 'question_web/admin_qes_body.html', {
            'qes_query': qes_query
    })
    # return render_mako_context(request, '/question_web/home.html', {
    #     'qes_query': qes_query
    # })

def qes_show(request, query_id):

    qes_query = Query_qes.objects.get(id=query_id)
    questions = Question.objects.all().filter(belong_id=query_id)
    return render_mako_context(request, '/question_web/qes_body.html', {
        #'question_name': 1,
        'qes_title':qes_query.name,
        'questions': questions,
        'num': questions.count()


    })





def admin_qes_delete(request, query_id):
    qes_query = Query_qes.objects.get(id=query_id)
    questions = Question.objects.all().filter(belong_id=query_id)
    return render_mako_context(request, '/question_web/admin_qes_delete.html', {
        # 'question_name': 1,
        'qes_title': qes_query.name,
        'questions': questions,
        'num': questions.count(),
        'id': query_id

    })


def admin_qes_delete_item(request,item_id):
    try:
        question = Question.objects.all().get(id=item_id)
        query_id = question.belong_id
        question.delete()
        query = Query_qes.objects.get(id=query_id)
        query.count= Question.objects.all().filter(belong_id=query_id).count()
        query.save()
        url = '/admin/qes_body/action/'
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


def admin_qes_action(request, query_id):
    qes_query = Query_qes.objects.get(id=query_id)
    questions = Question.objects.all().filter(belong_id=query_id)
    return render_mako_context(request, '/question_web/admin_qes_action.html', {
        # 'question_name': 1,
        'query_id':query_id,
        'qes_title': qes_query.name,
        'questions': questions,


    })

def admin_query_rename(request,query_id):
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




