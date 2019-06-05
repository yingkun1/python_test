"""
LEGB原则
python中作用域有四种
L(local):局部作用域
E(enclosing):闭包函数外的函数中
G(Global):全局作用域
B(Built-in):内建作用域
优先级：L>E>G>B
"""

# dir = 1 #这个是Global作用域的变量
# def outer():
#     dir  = 2 #这个是闭包函数外的函数中的作用域(Enclosing)
#     def inner():
#         dir = 3 #这个是局部作用域(Local)
#         return dir
#     return inner
#
# print(outer()())

"""
作用域(scope)和命名空间(namespace)
def/lambda会创建新的作用域，生成器表达式都有引入新的作用域
class的定义没有作用域，只是创建一个隔离的命名空间
在python中,scope是由namespace按特定的层次结构组合起来的，scope一定是namespace,但namespace不一定是scope
命名空间不能在里面再嵌套其他作用域
"""

# a = 1
# def test():
#     a += 1
#     a = 2
#
# test()


# class A(object):
#     x = 2
#     # gen = (A.x*i for i in range(5))
#     gen = (lambda x:(x*i for i in range(5)))(x)
# if __name__ == '__main__':
#     a = A()
#     print(list(a.gen))

"""
上面的代码会抛出异常：NameError: global name ‘x’ is not defined。这是因为gen = （x for _ in xrange(5）
是生成器，会产生新的作用域。而classA 中并不产生作用域。按照LEGB原则，不能找到x的定义，所以抛出异常。
解决这个问题有几种方案。
"""


# def test():
#     x = 2
#     gen = (x*i for i in range(5))
#     return gen
#
# gen = test()
# print(list(gen))