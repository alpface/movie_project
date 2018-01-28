# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 下午11:32
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : views.py
# @Software: PyCharm

from . import home
from flask import render_template, redirect, url_for

@home.route('/')
def index():
    return render_template('home/index.html')

# 登录
@home.route('/login/')
def login():
    return render_template('home/login.html')

# 退出
@home.route('/logout/')
def logout():
    # 退出时重定向到home模块下的login视图
    # url_for() 为路由生成器
    return redirect(url_for('home.login'))

@home.route('/register/')
def register():
    return render_template('home/register.html')