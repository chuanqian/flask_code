#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-08-31 11:34:42
# @Author  : qianchuan (qianchuan.zhang@yottatom.com)
# @Link    : http://www.zaqacu.com/
# @Version : $Id$
# @Description: 日志装饰器


def use_loggin(func):
    def wrapper(*args, **kwargs):
        print("[debug] %s is running" % func.__name__)
        return func(*args, **kwargs)

    # print(wrapper)
    return wrapper


@use_loggin
def bar():
    print("今天你开心吗？")


@use_loggin
def bar2():
    print("今天你快乐吗？")


# bar = use_loggin(bar)

bar()

# bar2 = use_loggin(bar2)
bar2()
