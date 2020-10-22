# -*- coding: utf-8 -*-
# @Time: 2020/10/16 10:22
# @Author: EDZ

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        return o.__dict__


class Flask(_Flask):
    json_encoder = JSONEncoder


def register_buleprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


# 初始化插件
def register_plugin(app):
    from app.model.base import db
    # 初始化数据库db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.secure")
    app.config.from_object("app.config.setting")
    # 注册蓝图
    register_buleprints(app)
    # 注册插件
    register_plugin(app)
    return app
