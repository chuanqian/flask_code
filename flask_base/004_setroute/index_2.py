# env python
# -*- coding: utf-8 -*-
# @Time: 2020/8/31 14:09
# @Author: EDZ
# @File: index_2.py
# @Software: PyCharm
# @Description: 第二种路由设置方式

from flask import Flask

app = Flask(__name__)


# 第一种
# @app.route("/hello")
def hellos():
    return "曹贼，拿命来！"


# 第二种
# @app.route("/hello/<user_name>")
def hello(user_name):
    return "i'm boy,%s" % user_name


# 第三种
app.add_url_rule(rule="/hello/kill", view_func=hellos)
app.add_url_rule(rule="/hello/user/<user_name>", view_func=hello)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
