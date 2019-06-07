"""
首先要了解,python中的对象包含的三个基本要素，分别是:id(身份标识)，type(数据类型)和value(值)
==:用来判断比较判断两个对象的value(值)是否相等
"""

# a = 'cheesezh'
# b = 'cheesezh'
# print(a==b)

"""
is比较判断的是对象间的唯一身份标识，也就是id是否相同
"""

x = y = [4,5,6]
z = [4,5,6]
print(id(x),id(y),id(z))
print(x==y)
print(x==z)
print(x is y)
print(x is z)


