"""
1.在协程中yield通常出现在表达式的右边，例如：datum = yield,可以产出值，
也可以不产出--如果yield关键字后面没有表达式，那么生成器产出None.

2.协程可能从调用方接受数据，调用方是通过send(datum)的方式把数据提供给协程使用，
而不是next(...)函数，通常调用方会把值推送给协程。

3.协程可以把控制器让给中心调度程序，从而激活其他的协程
"""

def simple_coroutine():
    print('-->coroutine started')
    x = yield
    print('-->coroutine received:',x)

my_coro = simple_coroutine()
# print(my_coro)
# next(my_coro)
my_coro.send(24)