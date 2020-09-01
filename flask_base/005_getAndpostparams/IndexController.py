# env python
# -*- coding: utf-8 -*-
# @Time: 2020/8/31 15:34
# @Author: EDZ
# @File: IndexController.py
# @Software: PyCharm
# @Description: 控制层


from flask import Blueprint,request

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index_page_index():
    return "index page"

@index_page.route("/get")
def get():
	var_a = request.args.get("a","I like eat furit.") if "a" in request.args else ""
	var_b = "method: %s, params: %s, var_a: %s" % (request.method,request.args,var_a)
	return var_b


@index_page.route("/post",methods = ["POST"])
def post():
	# var_a = request.form["a"] if "a" in request.form else ""
	# var_b = request.form["b"] if "b" in request.form else ""
	req = request.values
	var_a = req["a"] if "a" in req else ""
	var_b = req["b"] if "b" in req else ""
	return "method: %s, params: %s, var_a: %s, var_b: %s" % (request.method,req,var_a,var_b)

@index_page.route("/upload",methods = ["POST"])
def upload():
	file = request.files["a"] if "a" in request.files else None
	return "method: %s, params: %s,file: %s" % (request.method,request.files,file)
