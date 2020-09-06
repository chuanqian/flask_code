# 导入flask的类
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os

# 初始化Flask
app = Flask(__name__)

# 读取配置文件
app.config.from_pyfile("config/base_setting.py")

# flask设置环境变量
# ops_config=local|production|test
# Linux export ops_config=local|production
# Windows set ops_config=local|production
# 获取环境变量
# print(os.environ)
if "ops_config" in os.environ:
	app.config.from_pyfile("config/%s_setting.py"%(os.environ["ops_config"]))
else:
	print("not found")

manager = Manager( app )


# 数据库配置
db = SQLAlchemy(app)

app.logger.info("----------------")
