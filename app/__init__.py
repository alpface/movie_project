# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 下午11:28
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/movie"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SECRET_KEY"] = 'af2fad8cfe1f4c5fac4aa5edf6fcc8f3'
app.debug = True
db = SQLAlchemy(app)

# 注册蓝图
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

def page_not_found(error):
    return render_template('home/404.html'), 404