from enum import Enum


class ClientTypeEnums(Enum):
    # 邮箱登录
    USER_EMAIL = 100
    # 手机登录
    USER_MOBILE = 101

    # 小程序登录
    USER_MINA = 200
    # 微信
    USER_WX = 201
