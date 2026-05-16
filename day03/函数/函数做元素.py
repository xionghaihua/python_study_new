def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
ops = [add, sub, mul]
for func in ops:
    print(func(10, 3))

print("----------------------------")


def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

calc = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

# expr = input("请输入表达式>>>:")
# a,op,b = expr.split()
# result = calc[op](float(a), float(b))
# print(result)
print("---------------------")


