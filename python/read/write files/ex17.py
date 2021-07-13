#copy and paste
from sys import argv
from os.path import exists #exists将文件名字符串作为参数，判断其是否存在

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exsit? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

"""
echo "This is a test file." > test.txt
cat test.txt
python python\ex17.py python\test.txt python\new_file.txt
"""