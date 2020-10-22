# -*- coding: utf-8 -*-
# @Time: 2020/10/20 15:47
# @Author: EDZ
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        vaild = super(BaseForm, self).validate()
        if not vaild:
            raise ParameterException(msg=self.errors)
        return self
