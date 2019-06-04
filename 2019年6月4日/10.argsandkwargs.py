"""
当你不确定你的函数里将要传递多少参数时你可以用*args,例如。它可以传递任意数量的参数
"""
# def print_everything(*args):
#     for count,thing in enumerate(args):
#         print('{0}.{1}'.format(count,thing))
#
# print_everything('apple','banana','cabbage')

"""
相似的,**kwargs允许你使用没有事先定义的参数名
"""

# def table_thing(**kwargs):
#     for name,value in kwargs.items():
#         print("{0}={1}".format(name,value))
#
# table_thing(apple='fruit',cabbage = 'vegetable')

# def print_three_things(a,b,c):
#     print("a={0},b={1},c={2}".format(a,b,c))
#
# mylist = ['aardvark','baboon','cat']
# print_three_things(*mylist)

"""
    *args用来将参数打包成tuple给函数体调用
"""
# def function(*args):
#     print(args,type(args))
# function(1,2,3)

# def function(x,y,*args):
#     print(x,y,args)
#
# function(1,2,3,4,5)

"""
**kwargs:打包关键字参数成dict给函数体调用
"""

# def function(**kwargs):
#     print(kwargs,type(kwargs))
#
# function(a = 2)

# def function(**kwargs):
#     print(kwargs,type(kwargs))
#
# function(a = 1,b=2,c=3)

#综合
def function(arg,*args,**kwargs):
    print(arg,args,kwargs)

function(6,7,8,9,a=1,b=2,c=3)
