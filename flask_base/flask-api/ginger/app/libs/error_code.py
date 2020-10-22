# -*- coding: utf-8 -*-
# @Time: 2020/10/20 14:54
# @Author: EDZ

from app.libs.error import APIException


class ClientTypeException(APIException):
    code = 400
    msg = "client is params error"
    status = 1006


class ParameterException(APIException):
    code = 400
    msg = "invaild parameter"
    status = 1000


class ServerError(APIException):
    code = 500
    status = 500
    msg = "Global Exceptions"


class NotFound(APIException):
    code = 404
    status = 500
    msg = "Response Not Fount!"


class AuthFailed(APIException):
    code = 401
    status = 500
    msg = "this is not auth!"
