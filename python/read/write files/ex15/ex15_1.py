###
from sys import argv #调取模块

script, filename = argv
###
#上述代码用argv来获取文件名

txt = open(filename)
#接受一个参数，返回一个值，将这个值赋给一个变量 -> 打开文件

print(f"Here's your file {filename}:")
print(txt.read())#read() is a function & method

txt.close()