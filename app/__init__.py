# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 下午11:28
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask

app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')