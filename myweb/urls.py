#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: urls.py
@time: 2020/9/8 10:37
@desc: 
"""
from django.urls import path
from myweb import views

urlpatterns = [
    path('', views.queryLinux),
    path('queryLinuxs/', views.queryLinux),
    path('openAdd/', views.openAdd),
    path('saveLinux/', views.saveLinux),
    path('openEdit/', views.openEdit),
    path('updateLinux/', views.updateLinux),
    path('deleteLinux/', views.deleteLinux),
    path('daochu/', views.daochu),
    path('download/', views.download),
]
