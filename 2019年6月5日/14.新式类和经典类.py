"""
Python 2.x中默认都是经典类，只有显式继承了object才是新式类
python 3.x中默认都是新式类,经典类被移除，不必显式的继承object
"""

class A:
    def __init__(self):
        print("this is A")

    def save(self):
        print("save method from A")

class B(A):
    pass

class C(A):
    def save(self):
        print("save method from C")

class D(B,C):
    pass

d = D()
d.save()

"""
新式类很早在python2.2就出现了，所以经典类是一个兼容性的问题，现在主流的python3的类是新式类
新式类是根据C3算法，经典类深度优先
"""