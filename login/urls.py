# -*- coding: utf-8 -*-
from django.conf.urls import url
from login.views import login_home,login_to,register,register_action,test,login_out
urlpatterns = [
    url(r'^$', login_home),
    url(r'^login_to/$', login_to),
    url(r'^register/$', register),
    url(r'^register/action/$',register_action),
    url(r'^login_out/$', login_out)
]