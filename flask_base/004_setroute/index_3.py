# env python
# -*- coding: utf-8 -*-
# @Time: 2020/8/31 15:21
# @Author: EDZ
# @File: index_3.py
# @Software: PyCharm
# @Description: url配置，蓝图

from flask import Blueprint, Flask

app = Flask(__name__)
index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index_page_index():
    return "index page"


app.register_blueprint(index_page, url_prefix="/hello")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
