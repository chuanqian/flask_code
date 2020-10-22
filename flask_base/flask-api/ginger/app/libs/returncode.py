# -*- coding: utf-8 -*-
# @Time: 2020/10/20 16:30
# @Author: EDZ
from app.libs.error import APIException


class SuccessCode(APIException):
    code = 200
    status = 200
    msg = "success"
