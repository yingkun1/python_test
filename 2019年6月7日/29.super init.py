class A():
    def go(self):
        print("go A go")

    def stop(self):
        print("stop A stop")

    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B,self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C,self).go()
        print("go C go")

    def stop(self):
        super(C,self).stop()
        print("stop C stop")

class D(B,C):
    def go(self):
        super(D,self).go()
        print("go D go!")

    def stop(self):
        super(D,self).stop()
        print("stop D stop!")

    def pause(self):
        print("wait D wait!")

class E(B,C):
    pass

# a = A()
# a.go()

# b = B()
# b.go()

"""
继承的功能：父类代码的重用
多态的功能：同一方法对不同类型的对象会有不同的结果
开闭原则：对扩展开放，对修改封闭
super类功能：新式类实现广度优先算法，即c3算法
"""

# c = C()
# c.go()

# d = D()
# d.go()

e = E()
e.go()