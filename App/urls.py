# -*- encoding: utf-8 -*-
from django.urls import path

from App import views

app_name = "App"
urlpatterns = [
    path("curd/", views.handle_curd, name="curd"),
    path("add/", views.handle_add, name="add"),
    path("filter/", views.handle_filter, name="filter"),
    # 统计分组
    path("group/", views.handle_group, name="group"),
    #  原生SQL
    path("sql/", views.handle_sql, name="sql"),
]
