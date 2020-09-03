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
