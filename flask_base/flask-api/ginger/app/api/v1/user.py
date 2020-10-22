# from flask import Blueprint
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.model.user import User
from flask import jsonify

# user = Blueprint("user", __name__)
api = Redprint("user")


class QianChuan():
    age = 18
    name = "qianchuan"


@api.route("/get/<int:uid>", methods=["GET"])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(QianChuan())
