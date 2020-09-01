##### 1.安装Flask
```shell
pip install Flask
```
##### 2.Flask入门小例子
```python
# 创建一个文件HelloWorld
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
```
window启动访问
```shell
set FLASK_APP=HelloWorld.py
flask run
flask run --host=0.0.0.0
```
Linux启动访问
```shell
export FLASK_APP=HelloWorld.py
python flask run
python flask run --host=0.0.0.0
```
##### 3.网络配置
```python
from flask import Flask

app = Flask(__name__)
# 第一种方式-参数配置
app.config['DEBUG'] = True
# app.config.update(DEBUG=Ture,SECRET_KET='...')

# 第二种方式-模块配置
app.config.from_object('config.base_setting')

# 第三种方式-文件配置
app.config.from_pufile('config/base_setting.py')


@app.route("/")
def hello():
    return "I like flask"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888", debug=True)
```