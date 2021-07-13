"""
###
from sys import argv #调取模块

script, filename = argv
###
#上述代码用argv来获取文件名

txt = open(filename)
#接受一个参数，返回一个值，将这个值赋给一个变量 -> 打开文件

print(f"Here's your file {filename}:")
print(txt.read())#read() is a function & method
"""

print("Type the filename:")
file = input("> ")

txt = open(file)

print(txt.read())

txt.close()

"""
txt = open(filename)返回的是文件对象（file object），类似于磁带机，可以在内部任意移动，读取它们，文件对象并不是内容
"""