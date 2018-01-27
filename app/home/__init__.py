# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 下午11:30
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

home = Blueprint('home', __name__)

from app.home.views import *
