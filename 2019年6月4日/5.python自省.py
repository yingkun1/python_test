"""
    自省就是面向对象额语言所写的程序在运行时，所能知道对象的类型，就是运行是能够获得对象的类型，比如
    type(),dir(),getattr(),hasattr(),isinstance().

"""
a = [1,2,3]
b = {'a':1,'b':2,'c':3}
c = True
print(type(a),type(b),type(c))
print(isinstance(a,list))