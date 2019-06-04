class Myclass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world"

mc = Myclass()
try:
    # print(mc.__superprivate)
    print(mc._semiprivate)
except:
    print("没有这个变量")

# print(mc.__dict__)
print(mc._Myclass__superprivate)