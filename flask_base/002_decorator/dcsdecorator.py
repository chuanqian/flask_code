#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-08-31 11:49:46
# @Author  : qianchuan (qianchuan.zhang@yottatom.com)
# @Link    : http://www.zaqacu.com/
# @Version : $Id$
# @Description: 带参数的函数装饰器

def use_loggin(level="debug"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("[%s]%s is running" % (level, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@use_loggin("info")
def bar():
    print("带参数的装饰器。")


bar()
