"""
装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。
概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
"""

# def my_new_decorator(a_function_to_decorate):
#     def the_wrapper_function():
#         print("Befor the function runs")
#
#         a_function_to_decorate()
#
#         print("After the function runs")
#     return the_wrapper_function
#
# def a_stand_alone_function():
#     print("I am a stand alone function,don't you dare modify me")

# a_stand_alone_function()

# a_function_decorated = my_new_decorator(a_stand_alone_function)

# a_function_decorated()

# @my_new_decorator
#another_stand_alone_function = my_new_decorator(another_stand_alone_function)
# def another_stand_alone_function():
#     print("Leave me alone")
#
# another_stand_alone_function()


def a_decorator_passing_arguments(function_to_decorate):
    def a_warpper_accepting_arguments(arg1,arg2):
        print("I got args!Look:{},{}".format(arg1,arg2))
        function_to_decorate(arg1,arg2)
    return a_warpper_accepting_arguments

@a_decorator_passing_arguments
def print_full_name(first_name,last_name):
    print("My name is {} {} ".format(first_name,last_name))

print_full_name("Peter","VenkMan")


"""
装饰器的知识点
装饰器使函数调用变慢了.一定要记住.
装饰器不能被取消(有些人把装饰器做成可以移除的但是没有人会用)所以一旦一个函数被装饰了.所有的代码都会被装饰.
Python自身提供了几个装饰器,像property, staticmethod.
Django用装饰器管理缓存和试图的权限.
Twisted用来修改异步函数的调用.
"""