# env python
# -*- coding: utf-8 -*-
# @Time: 2020/8/31 15:31
# @Author: EDZ
# @File: application.py
# @Software: PyCharm
# @Description: 蓝图


from flask import Flask
from IndexController import index_page

app = Flask(__name__)

app.register_blueprint(index_page, url_prefix="/hello/qianchuan")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888", debug=True)
