# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 下午11:32
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : views.py
# @Software: PyCharm

from . import admin
from flask import render_template, redirect, url_for

# admin 主页
@admin.route('/')
def index():
    return render_template('admin/index.html')

# 登录
@admin.route('/login/')
def login():
    return render_template('admin/login.html')

# 退出
@admin.route('/logout/')
def logout():
    return redirect(url_for('admin.login'))

# 修改密码页面
@admin.route('/pwd/')
def pwd():
    return render_template('admin/pwd.html')
