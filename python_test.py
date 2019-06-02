# a = 1

# def fun(a):
#     a = 2

# fun(a)

# print(a)

# a = []

# def fun(a):
#     a.append(1)

# fun(a)

# print(a)

# a = 1
# print(id(a))
# def fun(a):
#     print("func_in",id(a))
#     a = 2
#     print("re-point",id(a),id(2))
# print("func_out",id(a),id(1))
# fun(a)
# print(a)

# a = []
# print(id(a))
# def fun(a):
#     print("func_in",id(a))
#     a.append(1)
#     print("re-point",id(a))
# print("func_out",id(a))
# fun(a)
# print(a)

"""
知识点1
python的函数参数传递
在python中，string,tuple，和numbers是不可更改的对象，
而list,dict,set等则是可以修改的对象，这就是这个问题的重点
当一个引用传递给函数的时候，函数自动复制一份引用，这个函数里面的引用和外边的引用没有关系，所以
第一个例子里的引用指向了一个不可变对象，但函数返回的时候，外边的引用没有感觉，而第二个
"""

# a = 1
# def fun(a):
#     a = 2
#     return a 
# fun(a)
# print(a)























