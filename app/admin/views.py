# -*- coding: utf-8 -*-
# @Time    : 2018/1/27 下午11:32
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : views.py
# @Software: PyCharm

from . import admin
from flask import render_template, redirect, url_for, flash, session, request
from app.admin.forms import LoginForm, TagForm
from app.models import Admin, Adminlog, Tag, Oplog
from app import db
from functools import wraps

# 登录装饰器
def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# admin 主页
@admin.route('/')
@admin_login_req
def index():
    return render_template('admin/index.html')

# 登录
@admin.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data['account']).first()
        if not admin.check_pwd(data['pwd']):
            flash('密码错误！', 'err')
            return redirect(url_for('admin.login'))
        session['admin'] = data['account']
        session['admin_id'] = admin.id
        adminlog = Adminlog(
            admin_id=admin.id,
            ip = request.remote_addr,
        )
        db.session.add(adminlog)
        db.session.commit()
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('admin/login.html', form=form)

# 退出
@admin.route('/logout/')
@admin_login_req
def logout():
    session.pop('admin', None)
    session.pop('admin_id', None)
    return redirect(url_for('admin.login'))

# 修改密码页面
@admin.route('/pwd/')
@admin_login_req
def pwd():
    return render_template('admin/pwd.html')

# 添加标签
@admin.route('/tag/add/', methods=['GET', 'POST'])
@admin_login_req
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag = Tag.query.filter_by(name=data['name']).count()
        if tag == 1:
            flash("名称已存在！", "err")
            return redirect(url_for('admin.tag_add'))
        tag = Tag(
            name=data['name']
        )
        db.session.add(tag)
        db.session.commit()
        flash('添加标签成功', 'ok')
        oplog = Oplog(
            admin_id=session['admin_id'],
            ip = request.remote_addr,
            reason='添加标签%s' % data['name']
        )
        db.session.add(oplog)
        db.session.commit()
        redirect(url_for('admin.tag_add'))
    return render_template('admin/tag_add.html', form=form)

# 标签列表
@admin.route('/tag/list/<int:page>/', methods=['GET'])
@admin_login_req
def tag_list(page=None):
    if page == None:
        page = 1
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=page, pre_page=10)
    return render_template('admin/tag_list.html', page_data=page_data)

# 添加电影
@admin.route('/movie/add')
@admin_login_req
def movie_add():
    return render_template('admin/movie_add.html')

# 电影列表
@admin.route('/movie/list/')
@admin_login_req
def movie_list():
    return render_template('admin/movie_list.html')

# 添加预告
@admin.route('/preview/add')
@admin_login_req
def preview_add():
    return render_template('admin/preview_add.html')

# 预告列表
@admin.route('/preview/list/')
@admin_login_req
def preview_list():
    return render_template('admin/preview_list.html')


# 会员列表
@admin.route('/user/list')
@admin_login_req
def user_list():
    return render_template('admin/user_list.html')

# 查看会员
@admin.route('/user/view/')
@admin_login_req
def user_view():
    return render_template('admin/user_view.html')

# 评论列表
@admin.route('/comment/list/')
@admin_login_req
def comment_list():
    return render_template('admin/comment_list.html')

# 收藏列表
@admin.route('/moviecol/list/')
@admin_login_req
def moviecol_list():
    return render_template('admin/moviecol_list.html')

# 操作日志
@admin.route('/oplog/list/')
@admin_login_req
def oplog_list():
    return render_template('admin/oplog_list.html')

# 管理员登录日志
@admin.route('/adminloginlog/list/')
@admin_login_req
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')

# 会员登录日志
@admin.route('/userloginlog/list/')
@admin_login_req
def userloginlog_list():
    return render_template('admin/userloginlog_list.html')

# 角色列表
@admin.route('/role/list/')
@admin_login_req
def role_list():
    return render_template('admin/role_list.html')

# 添加角色
@admin.route('/role/add/')
@admin_login_req
def role_add():
    return render_template('admin/role_add.html')

# 权限列表
@admin.route('/auth/list/')
@admin_login_req
def auth_list():
    return render_template('admin/auth_list.html')

# 添加权限
@admin.route('/auth/add/')
@admin_login_req
def auth_add():
    return render_template('admin/auth_add.html')


# 管理员列表
@admin.route('/admin/list/')
@admin_login_req
def admin_list():
    return render_template('admin/admin_list.html')

# 添加管理员
@admin.route('/admin/add/')
@admin_login_req
def admin_add():
    return render_template('admin/admin_add.html')
