from application import app
from controllers.index import index_page
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension(app)

# 蓝图注册地址
app.register_blueprint(index_page,url_prefix="/")