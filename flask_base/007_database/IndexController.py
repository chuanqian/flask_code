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

