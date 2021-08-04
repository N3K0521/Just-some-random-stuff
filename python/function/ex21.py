#return将变量设置成“一个函数的值”
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} + {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height： {height}, Weight： {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
"""
iq = divide(100, 2) = 50
divide(iq, 2) = divide(50, 2) = 25
weight = multiply(90, 2) = 180
multiply(weight, 25) = 180 * 25 = 4500
height = subtract(78, 4) = 74
subtact(74, 4500) = -4426
age = add(30, 5) = 35
what = add(35, -4426) = -4391
"""

print("That becomes: ", what, "Can you do it by hand?")

#用input（）输入自己的值：
#int(input()) -> integers
#float(input()) - > float