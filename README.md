# Flask 搭建的视频网站学习记录

使用蓝图构建项目目录

#### 运行项目
- 创建基于python3.6的虚拟环境`movie_venv`:
```
mkvirtualenv -p /usr/local/bin/python3 movie_venv
```
激活虚拟环境
```angular2html
source ~/movie_venv/bin/activate
```

注意: `/usr/local/bin/python3`为python3的路径，如果不确定可以使用: which python3查找
- 激活虚拟环境:`source ~/movie_venv`
- 安装依赖包:
```
pip3 install flask
pip3 install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com flask-sqlalchemy
pip3 install Flask-WTF
```

#### 创建数据库
登录mysql
```
mysql -uroot -p
```
创建名称为movie的数据库
```
create database movie chartset=uft8;
```

根据models创建表， 在models.py中添加一下代码，并运行model.py：
```
if __name__ == "__main__":
    db.create_all()

    role = Role(
        name="超级管理员",
        auths="1111"
    )
    db.session.add(role)
    db.session.commit()
    from werkzeug.security import generate_password_hash

    admin = Admin(
        name="alpface",
        pwd=generate_password_hash("alpface"),
        is_super=0,
        role_id=1
    )
    db.session.add(admin)
    db.session.commit()
```




