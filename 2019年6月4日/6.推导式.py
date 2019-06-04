"""
    1.列表推导式
    2.字典推导式
    3.集合推导式
"""

# multiples = [i for i in range(30) if i%3 is 0]
# print(multiples)

# items = [4, 3, 2, 7, 8, 2, 3, 1, 2]
# result = {item for item in items if items.count(item)>1}
# print(result)

# def squared(x):
#     return x*x
# multiples = [squared(i) for i in range(30) if i%3 is 0]
# print(multiples)

# multiples = (i for i in range(30) if i % 3 is 0 )
# print(type(multiples))
# print(multiples)

# mcase = {'a':10,'b':34,'A':7,'Z':3}
# print(mcase.keys())
# print(mcase.get('a',0))
# mcase = {'a':10,'b':34,'A':7,'Z':3}
# macse_frequency = {
#     k.lower():mcase.get(k.lower(),0) + mcase.get(k.upper(),0)
#     for k in mcase.keys()
#     if k.lower() in ['a','b']
# }
# print(macse_frequency)

# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# mcase_frequency = {
#     k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
#     for k in mcase.keys()
#     if k.lower() in ['a','b']
# }
# print(mcase_frequency)

# mcase = {'a':10,'b':34}
# mcase_frequency = {v:k for k,v in mcase.items()}
# print(mcase_frequency)

# mcase = {'a': 10, 'b': 34}
# mcase_frequency = {v: k for k, v in mcase.items()}
# print(mcase_frequency)

# squared = {x**2 for x in [1,1,2]}
# print(squared)