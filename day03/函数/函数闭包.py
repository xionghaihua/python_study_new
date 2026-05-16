"""
有嵌套函数（内层函数）
内层函数饮用外层变量
外层函数返回内层函数
"""

def outer():
    x = 10
    def inner():
        print(x)
    return inner
fn = outer()
fn()

#计数器
def make_counter(start=0):
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
counter = make_counter()
print(counter())
print(counter())
print("==========================")
#累加器
def make_accumulator():
    total = 0
    def add(n):
        nonlocal total
        total += n
        return total
    return add
acc = make_accumulator()
print(acc(10))  # 10
print(acc(20))  # 30
print(acc(5))  # 35
print("==========================")