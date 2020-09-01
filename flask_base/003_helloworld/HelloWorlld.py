# env python
# -*- coding: utf-8 -*-
# @Time: 2020/8/27 16:43
# @Author: EDZ
# @File: HelloWorlld.py
# @Software: PyCharm
# @Description: Flask的HelloWorld

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "I like flask"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888", debug=True)
