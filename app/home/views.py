# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 下午11:32
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : views.py
# @Software: PyCharm

from . import home
from flask import render_template

@home.route('/')
def index():
    return render_template('home/index.html')