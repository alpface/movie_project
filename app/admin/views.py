# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 下午11:32
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : views.py
# @Software: PyCharm

from . import admin

@admin.route('/')
def index():
    return "<h1 style='color:red'>this is admin</h1>"