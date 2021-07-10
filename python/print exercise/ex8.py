formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

'''
formatter.format(...) -> 函数，令其返回formatter变量到其他字符串中
1. 取第一行定义的formatter字符串
2. 调用它的format函数，这相当于告诉他执行一个叫format的命令行命令
3. 给format传递4个参数，这些参数和formatter变量中的{}匹配，相当于将参数传递给了format这个命令
4. 在formatter上调用format的结果是一个新字符串，其中的{}被4个变量替换掉了，这就是print现在打印出的结果
'''