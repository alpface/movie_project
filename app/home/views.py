# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 下午11:32
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : views.py
# @Software: PyCharm

from . import home
from flask import render_template, redirect, url_for

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

# 会员中心
@home.route('/user/')
def user():
    return render_template('home/user.html')

# 修改密码
@home.route('/pwd/')
def pwd():
    return render_template('home/pwd.html')

# 评论页面
@home.route('/comments/')
def comments():
    return render_template('home/comments.html')

# 登录日志
@home.route('/loginlog/')
def loginlog():
    return render_template('home/loginlog.html')

# 收藏页面
@home.route('/moviecol/')
def moviecol():
    return render_template('home/moviecol.html')

# 主页
@home.route('/')
def index():
    return render_template('home/index.html')

# 动画
@home.route('/animation/')
def animation():
    return render_template('home/animation.html')

# 搜索
@home.route('/search/')
def search():
    return render_template('home/search.html')



