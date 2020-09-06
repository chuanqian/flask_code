from application import app
from controllers.index import index_page
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension(app)

# 拦截器处理 和错误拦截器
from interceptors.Auth import *
from interceptors.errorHandler import *

# 蓝图注册地址
app.register_blueprint(index_page,url_prefix="/")