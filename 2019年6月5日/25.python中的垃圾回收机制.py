"""
python GC主要使用引用计数(reference counting)来跟踪和回收垃圾.在引用技术的基础上，通过标记-清除解决容器对象可能产生的
循环引用问题，通过分代回收，以空间换时间的方法提高垃圾回收效率
非常棒的一篇博客“https://www.cnblogs.com/pinganzi/p/6646742.html”
1.引用计数
2.标记清除
3.分代计数

"""