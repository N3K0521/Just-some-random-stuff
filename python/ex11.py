print("How old are you?", end = '')
age = input()
print("How tall are you?", end = '')
height = input()
print("How much do you weight?", end = '')
weight = input()

# x = int(input()): 从input() 获取字符串形式的数值，然后用int() 把它转换成整数。 

print(f"So, you're {age} old, {height} tall and {weight} heavy.")