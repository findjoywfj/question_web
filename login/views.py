# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from question_web.mymako import render_mako_context
from login.models import User,User_mongo
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from mongoengine.errors import DoesNotExist

from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
# Create your views here.
def login_home(request):
    return render_mako_context(request, '/question_web/login.html')

def login_to(request):
    try:
        name = request.POST["name"]
        password = request.POST["password"]
        role = User_mongo.objects.get(name=name).role
        key_data = User_mongo.objects.get(name=name).password
        request.session["name"] = name
        request.session["role"] = role
        if key_data == password:
            if role == 0:
                return JsonResponse({
                    'result':True,
                    'message':u'登陆成功 管理员您好！',
                    'data': 'developer/'
                })
            elif role == 1:
                return JsonResponse({
                    'result': True,
                    'message': u'登陆成功 开始测试吧',
                    'data': 'customer/'
                })
        else:
            return JsonResponse({
                'result': False,
                'message': u"用户名获密码错误",
            })
    except Exception as e:
        return JsonResponse({
            'result': False,
            'message': u'登陆失败'

        })


def register(request):
    return render_mako_context(request, 'question_web/register.html')


def register_action(request):
    name = request.POST["name"]
    password = request.POST["password"]
    try:
        User_mongo.objects.get(name=name)
        return JsonResponse({
            'result': False,
            'message': '用户名已存在'
        })
    except DoesNotExist:
        new_user = User_mongo(name=name,password=password,role=1)
        new_user.save()
        return JsonResponse({
            'result': True,
            'message':'注册成功！'
        })
    except Exception as e:
        return JsonResponse({
            'result': False,
            'message': '注册失败'
        })

def login_out(request):
    try:
        del request.session["name"]
        del request.session["role"]
        return HttpResponseRedirect("/")
    except Exception as e:
        return HttpResponseRedirect("/")
def test(request):
        # name = request.POST["name"]
        # password = request.POST["password"]
        Question_mongo.objects.create(name = {"name": "wfj", "passward": "123"})
        return HttpResponse("OK")