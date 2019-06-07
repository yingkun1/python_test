"""
通常，你在某处就真的只需要一个能做一件事情的函数而已,连它叫什么名字都无关紧要，lambda表达式就可以用来做这件事
"""
# map(lambda x:x*x,[y for y in range(10)])

a = [1,2,3]

f = lambda x : x+1

print(map(f,a))

map(lambda x : x+1,[1,2,3])