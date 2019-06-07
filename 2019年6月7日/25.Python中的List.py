L = []
L.append(1)
L.append(2)
L.append(3)
# print(L)

for e in L:
    print(e)

"""
typedef struct {
    PyObject_VAR_HEAD
    PyObject **ob_item  #保存元素的指针数组
    Py__ssize_t allocated   #预先分配的内存总容量
}
"""
