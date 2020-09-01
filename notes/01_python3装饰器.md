#### Python3装饰器
##### 概念
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动得前提下增加额外功能，装饰器的返回值也是一个函数对象，他经常用于又切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
##### 常见的装饰器
内置装饰器、类装饰器、函数装饰器、带参数的函数装饰器

```python
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
```
带参数函数装饰器
```python
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
```