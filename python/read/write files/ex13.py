# 脚本 -> .py程序
# 命令python python\ex12.py中的ex12.py就是参数(argument)
# 此脚本可以接收参数

from sys import argv #这行将python的特性(即模块module，或称之为库library)引入脚本，调用模块
                     #argv是参数变量 argument variable，该变量保存着python脚本运行时传递给python脚本的参数
# read the WYSS section for hwo to run this
script, first, second, third = argv #这行将argv解包(unpack)，赋值参数给4个变量。
                                    #定义：把argv中的东西取出，解包，将所有的参数依次赋值给左边的这些变量

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)