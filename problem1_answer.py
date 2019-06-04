"""
给一个数组，数组内的元素是整数，找出其中重复出现过的整数，返回以这些重复的整数为元素组成的新数组，顺序无所谓。
例如，给定[4,3,2,7,8,2,3,1,2]，应该返回[2,3]或者[3,2]
"""


# def find_dup(items: list) -> list:
    #方法一：
    # seen = set()
    # duplicated = set()
    # for x in items:  
    #     if x not in seen:  
    #         seen.add(x)
    #     else:
    #         duplicated.add(x)
    # return  list(duplicated)

    #方法二：
    # result = []
    # for item in items :
    #     if items.count(item)>1:
    #         result.append(item)
    # return (list(set(result)))

# if __name__ == "__main__":
#     result = find_dup([4, 3, 2, 7, 8, 2, 3, 1, 2])
#                       # [8,3,2,7,4,2,3,1,2]
#     assert result == [2, 3] or result == [3, 2]
#     print("OK")
