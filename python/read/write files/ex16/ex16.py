"""
close: 关闭文件。类似于编辑器中的“文件”->“保存”
read: 读取文件内容，把结果赋给一个变量
readline: 读取文本文件中的一行
truncate: 清空文件
write('stuff'): 将"stuff"写入文件
seek(0): 将读写位置移动到文件开头
"""

#数据存在于要求线性读写的介质（唱片，卡带）上
#磁带/dvd驱动器需要搜索（seek）某个特定位置，并可以从该位置开始读写
#我们的操作系统和文件系统已经模糊了随机访问存储和磁盘之间的界限
#write需要接收一个字符串作为参数，从而将该字符串写入文件

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file.   Goodbye!")
target.truncate() #truncating the file if it already exists

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
target.write(line1+"\n"+line2+"\n"+line3+"\n")

print("And finally, we close it.")
target.close()

"""
'w'是一个字符的特殊字符串，用来表示文件的访问模式，即“写入”（write）模式
'r'表示“读取”（read）
'a'表示“追加”（append）

修饰符使用案例：
'w+', 'r+', 'a+'

open()函数的默认行为是使用'r'只读模式打开文件
"""

"""
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
"""