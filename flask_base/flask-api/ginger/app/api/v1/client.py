from app.libs.redprint import Redprint
from app.validators.froms import ClientFrom, UserEmailFrom
from app.libs.enums import ClientTypeEnums
from app.model.user import User
from app.libs.returncode import SuccessCode

api = Redprint("client")


@api.route("/register", methods=["POST"])
def create_client():
    form = ClientFrom().validate_for_api()
    promise = {
        ClientTypeEnums.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return SuccessCode()
    # 传参的方式：表单（表单）、json（移动端）
    # 注册 登录
    # 参数 校验 接收参数
    # WTForms 验证表单


def __register_user_by_email():
    form = UserEmailFrom().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
