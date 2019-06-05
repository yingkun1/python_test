"""
单例模式：是一种常用的软件设计模式，在它的核心结构中只包含一个被称为单例类的特殊类，通过单例模式可以保证系统中一个
类只有一个实例易于外界访问，从而方便对实例个数的控制并节约系统资源，如果希望在系统中某个类的对象只能存在一个，单例模式
是最好的解决方案

__new__()在__init__()之前被调用,用于生成实例对象，利用这个方法和类的属性特点可以实现设计模式的单例模式。
单例模式是指创建唯一对象
"""

#1.使用模块
# from test.mysingleton import my_singleton
# my_singleton.foo()

#2,使用__new__,为了使类只能出现一个实例,我们可以使用__new__来控制实例的创建过程,代码如下
# class Singleton(object):
#     _instance = None
#
#     def __new__(cls, *args, **kw):
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
#         return cls._instance
#
#
# class MyClass(Singleton):
#     a = 1
#
# one = MyClass()
# two = MyClass()
# print(one==two)
# print(id(one),id(two))

"""
3.使用装饰器
"""

# from functools import wraps
#
# def singleton(cls):
#     instances = {}
#     @wraps(cls)
#     def getinstance(*args,**kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args,**kwargs)
#         return instances[cls]
#     return getinstance
#
# @singleton
# class MyClass(object):
#     a = 1
#
# one = MyClass()
# two = MyClass()
# print(one==two)
# print(id(one),id(two))

#4.使用metaclass
"""
元类(metaclass)可以控制类的创建过程，它主要做三件事
1.拦截类的创建
2.修改类的定义
3.返回修改后的类
使用元类实现单例模式的代码如下：
"""


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
    pass

one = MyClass()
two = MyClass()
print(one==two)
print(id(one),id(two))

"""
总结:python的模块是天然的单例模式，在大部分情况下已经足够使用，当然，我们也可以使用装饰器，元类，__new__方法等
参考：http://python.jobbole.com/87294/
"""