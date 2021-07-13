from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file {filename}:")
print(txt.read())
txt.close()
#method 2
"""
print("Type the filename:")
file = input("> ")

txt = open(file)

print(txt.read())
txt.close()
"""