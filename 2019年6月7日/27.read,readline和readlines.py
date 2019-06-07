# f = open(r"C:\Users\H\Desktop\a.txt")
# lines = f.read()
# print(lines)
# print(type(lines))
# f.close()

# f = open(r"C:\Users\H\Desktop\a.txt")
# line = f.readline()
# print(type(line))
#
# while line:
#     print(line)
#     line = f.readline()
#
# f.close()

# f = open(r"C:\Users\H\Desktop\a.txt")
# lines = f.readlines()
# print(type(lines))
# for line in lines:
#     print(line)
#
# f.close()

import linecache

text = linecache.getline(r"C:\Users\H\Desktop\a.txt",2)
print(text)