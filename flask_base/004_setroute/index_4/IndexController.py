# env python
# -*- coding: utf-8 -*-
# @Time: 2020/8/31 15:34
# @Author: EDZ
# @File: IndexController.py
# @Software: PyCharm
# @Description: 控制层


from flask import Blueprint

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index_page_index():
    return "index page"
