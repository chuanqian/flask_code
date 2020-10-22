from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp
from app.libs.enums import ClientTypeEnums
from app.model.user import User
from app.validators.base import BaseForm as Form
from app.libs.error_code import ParameterException


class ClientFrom(Form):
    account = StringField(validators=[DataRequired(), length(
        min=5, max=32
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnums(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailFrom(ClientFrom):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[
        DataRequired(),
        length(min=2, max=22)
    ])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ParameterException(msg="this account is not unique!", status=401)
