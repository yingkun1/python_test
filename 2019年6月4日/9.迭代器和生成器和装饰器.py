"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
"""

# L = [x*x for x in range(10)]
# print(type(L)
# print(L)
#
# G = (x*x for x in range(10))
# print(type(G))
# print(G)
# while next(G)<49:
#     print(next(G))
# for n in G:
#     print(n,end=";")

# it = iter([1,2,3])
# print(next(it))
#
# print(next(it))
#
# print(next(it))
#
# print(next(it))

# a = [0,1,2,3,4,5,6,7,8,9]
# for index,i in enumerate(a):
#     a[index] += 1
#
# print(a)

# a = [0,1,2,3,4,5,6,7,8,9]
# a = map(lambda x:x+1,a)
# print(type(a))
# print(a)
# print(list(a))

# def myYield(n):
#     while n > 0:
#         print('开始生成...')
#         yield n
#         print('完成一次...')
#         n -= 1
#
# if __name__ == '__main__':
#     a = myYield(3)
#     print('已经实例化生成器对象')
#     a.__next__()
#     print("第二次调用__next__()方法")
#     a.__next__()

# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b,a+b
#         n = n+1
#         return 'done'
#
# fib(5)
