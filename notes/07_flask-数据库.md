#### flask中集成数据库
##### 安装的依赖
```shell
	pip install flask-sqlalchemy
	pip install mysqlclient
```
##### 数据库配置
```python
# application.py
# 导入flask的类
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from IndexController import index_page

# 初始化Flask
app = Flask(__name__)

# 数据库配置
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@115.29.187.120/mysql"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_COMMIT_TEARDOWN"] =True
db = SQLAlchemy(app)

# 蓝图注册地址
app.register_blueprint(index_page,url_prefix="/qianchuan")

if __name__=="__main__":
	app.run(host="0.0.0.0",port="8887",debug=True)
```
##### 拆分application.py
```python
# 将application.py文件拆分成文件manage.py核心管理类，www.py 视图管理类 application.py 配置类,避免文件引入冲突问题

# application.py
# 导入flask的类
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 初始化Flask
app = Flask(__name__)

# 数据库配置
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@115.29.187.120/mysql"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_COMMIT_TEARDOWN"] =True
db = SQLAlchemy(app)

# manage.py
from application import app
from www import *

if __name__=="__main__":
	app.run(host="0.0.0.0",port="8887",debug=True)

# www.py
from application import app
from IndexController import index_page

# 蓝图注册地址
app.register_blueprint(index_page,url_prefix="/qianchuan")
```
##### models
```python
from flask import Blueprint,request,make_response,jsonify,render_template
from application import db
from sqlalchemy import text
from common.model.user import User
import json

# 初始化蓝图路由配置
index_page = Blueprint("index_page",__name__)

# 查询mysql数据库的用户
@index_page.route("/getUser")
def queryUser():
	contend = {}
	print("enter")
	sql = text( "select * from `user`" )
	results = db.engine.execute( sql )
	# for imter in results:
	# 	contend[imter["User"]] = imter["User"]
	# 	print("1111"+imter["User"])
	# print(results)
	contend["results"] = results
	print(contend)
	return make_response(jsonify({"a":"b"}))

# 使用model查询数据
@index_page.route("/getUserByModel")
def getUserByModel():
	results = User.query.all()
	print(results)
	contend = {}
	# resultjson = json.dumps(results)
	contend["results"] = resultjson
	return make_response(jsonify(contend))
```
##### model生成数据库表
```python
# user.py
# coding: utf-8
# from sqlalchemy import Column, DateTime, Integer, JSON, LargeBinary, SmallInteger, String, Text
# from sqlalchemy.schema import FetchedValue
# from sqlalchemy.dialects.mysql.enumerated import ENUM
# from flask_sqlalchemy import SQLAlchemy
from application import db

# db = SQLAlchemy()




class User(db.Model):
    __tablename__ = 'user'

    Host = db.Column(db.String(255, 'ascii_general_ci'), primary_key=True, nullable=False, server_default=db.FetchedValue())
    User = db.Column(db.String(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=db.FetchedValue())
    User_attributes = db.Column(db.JSON)


# manage.py
from application import app,db
# from www import *

if __name__=="__main__":
	from common.models.user import User
	print("0")
	db.create_all()
	# app.run(host="0.0.0.0",port="8887",debug=True)

# application.py
# 导入flask的类
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 初始化Flask
app = Flask(__name__)

# 数据库配置
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@115.29.187.120/tem_test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_COMMIT_TEARDOWN"] =True
db = SQLAlchemy(app)
```
##### 根据数据库表生成model
```shell
<!-- 在根目录下运行语句 -->
flask-sqlacodegen "mysql://root:123456@115.29.187.120/mysql" --table user --outfile "common/models/user.py" --flask
```