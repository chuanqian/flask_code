# env python
# -*- coding: utf-8 -*-
# @Time: 2020/8/31 15:34
# @Author: EDZ
# @File: IndexController.py
# @Software: PyCharm
# @Description: 控制层


from flask import Blueprint,request,make_response,jsonify,render_template
import json

index_page = Blueprint("index_page", __name__)

@index_page.route("/text")
def text():
	return "text/html"

@index_page.route("/text_same")
def text_same():
	return "text/html",200

@index_page.route("/jsons")
def jsons():
	data= {"a":"b"}
	response = make_response(json.dumps(data))
	response.headers["Content-Type"]="application/json"
	return response

@index_page.route("/json_same")
def json_same():
	data={"a":"b"}
	response = make_response(jsonify(data))
	return response


# 模板
@index_page.route("/templates")
def templates():
	return render_template("hello.html")

# 模板中传递变量(方式1)
@index_page.route("/templates_cdbl1")
def templates_cdbl1():
	name = "你今天还好吗？"
	return render_template("hello.html",name=name)

#模板中传递变量(方式2)
@index_page.route("/templates_cdbl2")
def templates_cdbl2():
	name = "你今天高兴吗？"
	context = {"name":name}
	return render_template("hello.html", **context)


#模板中传递变量(方式3)
@index_page.route("/templates_cdbl3")
def templates_cdbl3():
	context = {}
	context["user"] = {"name":"name","qq":"1178995389@qq.com","main":"https://www.cnblogs.com/qianchuan/"}
	context["tem_num"] = [1,2,3,4,5]
	return render_template("hello.html", **context)

# 模板继承
@index_page.route("/extend_template")
def extend_template():
	return render_template("extend_template.html")
