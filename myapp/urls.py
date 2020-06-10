# -*- encoding: utf-8 -*-
"""
@File    : urls.py
@Time    : 2020/6/10 10:11
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from django.conf.urls import url

# 导入试图模块
from myapp import views

urlpatterns = [
    # 对于路由执行对应模块中的视图
    url(r'^index/$', views.index),
    # 展示所有班级
    url(r'^grades/$', views.grades),
    # 展示所有学生
    url(r'^students/$', views.students),
    # 查看具体某个学生的详细详细
    url(r'^studentsDetail/(\d+)$', views.studentDetail),
    # 展示某个班级的学生
    url(r'^students/(\d+)$', views.gstudents),
]