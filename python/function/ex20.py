from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) #将读写位置移动到文件开头

def print_a_line(line_count, f):
    print(line_count, f.readline()) #readline()会扫描文件的每一个字节，直到找到\n为止，然后停止读取文件，并返回此前发现的文件内容
    #文件f会记录每次调用readline（）后的读取位置，以便下次调用时读取下一行

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
#current_line = line_count = 1, current_file = f.readline()

current_line = current_line + 1
print_a_line(current_line, current_file)
#current_line = 1 + 1 = 2 

current_line += 1
print_a_line(current_line, current_file)
#current_line = 2 + 1 = 3

"""
readline（）函数返回的内容中包含文件本来就有的\n， print时再加一个，所以结果会空一行
def print_a_line(line_count, f):
    print(line_count, f.readline(), end="") 
就可以解决
"""