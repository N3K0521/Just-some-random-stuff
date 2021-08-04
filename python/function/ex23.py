"""
1. 现代计算机如何存储人类语言，并进行显示或者处理。python3将其称之为字符串string
2. 如何把python的字符串编码和解码为一个叫字节串bytes的类型
3. 如何处理在字符串和字节处理中出现的错误
4. 如何阅读代码，弄明白你看到的新东西
"""

import sys
scripts, encoding, error = sys.argv
#命令行参数处理

def main(language_file, encoding, errors):
#主函数main将在脚本的结尾被调用
    line = language_file.readline()
    #从给该脚本的语言文件中读取一行

    if line:
    #检验一行内容中是否包含某样东西， 运行到文件结尾时，readline函数会返回一个空字符串，这个if用来检查这个空字符串
    #如果readline返回了内容，这里就会true，下面代码就会执行；如果false，下两行代买被跳过
        print_line(line, encoding, errors)
        #调用了另一个函数print_line()来实际打印这一行
        return main(language_file, encoding, errors)
        #在main里又调用了一次main -> 循环
        #if语句在此处的功能是防止该函数永远循环下去


def print_line(line, encoding, errors):
#定义print_line函数，实际上是对language.txt中每一行进行编码
    next_lang = line.strip()
    #把每一行结尾的\n删掉
    raw_bytes = next_lang.encode(encoding, errors = errors)
    #取到了language.txt中的语言，把它编码成原始字节。DBES解码字节串，编码字节串
    #next_lang变量是一个字符串
    #要获取原始字节串，必须调用.encode()来编码字符串
    #把需要的编码方式和处理错误的方式传入encode()函数
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    #展示了上一行的逆操作，从raw_bytes创建了一个cooked_string变量
    #DBES —> 字节串需要解码，raw_bytes就是字节串，所以调用了.decode()，从而得到一个python字符串
    #该字符串和next_lang变量是一样的

    print(raw_bytes, "<===>", cooked_string)
    #打印二者

languages = open("python\languages.txt", encoding = "utf-8")
#函数定义完成，打开languages.txt文件

main(languages, encoding, error)
#执行main函数

#command: python python\ex23.py utf-8 strict