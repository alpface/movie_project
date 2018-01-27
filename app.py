# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 下午11:14
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : app.py
# @Software: PyCharm

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1 style="color:red">hello world</h1>'

if __name__ == '__main__':
    app.run()