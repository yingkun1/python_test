"""
range函数说明:range([start,]stop[,step])，根据start与stop指定的范围以及step的步长
生成一个序列
xrange函数说明：用法与range完全相同，所不同的是生成的不是一个数组，而是一个生成器
当生成很大的数字序列的时候，用xrange会比range性能优很多因为不需要一上来就开辟一块很大
的内存空间，这两个基本上都是在循环的时候用
"""