# Flask 搭建的视频网站学习记录

使用蓝图构建项目目录

#### 运行项目
- 创建基于python3.6的虚拟环境`movie_venv`:
```
mkvirtualenv -p /usr/local/bin/python3 movie_venv
```
注意: `/usr/local/bin/python3`为python3的路径，如果不确定可以使用: which python3查找
- 激活虚拟环境:`source ~/movie_venv`
- 安装依赖包:
```
pip3 install flask
pip3 install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com flask-sqlalchemy

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


