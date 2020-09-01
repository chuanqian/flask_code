#### URL路由配置
##### 第一类
```python
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
```
##### 第二类：蓝图
```python
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
```
**蓝图可拆分层数**
```python
# 第一个文件IndexController.py,里边又index_page
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
```
```python
# 第二个文件application.py
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

app.register_blueprint(index_page, url_prefix="/hello/index")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
```
```python
# 解决问题if __name__ == "__main__": ····
# 答: 为了防止导入的时候其他模块执行此模块的函数
```