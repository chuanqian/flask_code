from application import app
from IndexController import index_page


# 蓝图注册地址
app.register_blueprint(index_page,url_prefix="/qianchuan")