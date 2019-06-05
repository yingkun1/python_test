"""
有了嵌套函数这种结构，便会产生闭包问题
闭包=函数+引用环境
闭包会把函数和运行时的引用环境打包成为一个新的整体，所以就解决了函数编程中的嵌套所引发的问题
由闭包生成的实例是隔离的，分别包含调用时不同的引用环境现场

python中闭包的定义：如果在一个内部函数里，对外部作用域(不是全局作用域LEGB中E作用域)的变量进行引用，
那么内部函数就被认为是闭包(closure)
"""

# def ExFunc(n):
#     sum = n
#     def InFunc():
#         return sum + 1
#     return InFunc
#
# myFunc = ExFunc(10)
# print(type(myFunc()))
# print(myFunc())

# def addx(x):
#     def addr(y):
#         return(x+y)
#     return addr
#
# c = addx(8)
# print(type(c))
# print(c.__name__)
# print(c(10))

# def foo():
#     m = 0
#     def foo1():
#         m = 1
#         print(m)
#     print(m)
#     foo1()
#     print(m)
#
# foo()

def foo():
    a = 1
    def bar():
        a = a + 1
        return(a)
    return bar

foo()()