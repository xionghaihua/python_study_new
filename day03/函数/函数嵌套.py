#内层函数可以读取外层函数的变量，但不能直接修改，修改需要nonlocal
def greet(name):
    def say():
        print(f"Hello {name}")
    return say
say = greet("alex")
say()
print("----------------------------------------")

#封装，隐藏内部实现
def process_data(data):
    def clean(s):
        return s.strip().lower()
    def validata(s):
        return s.isalnum()
    result = []
    for item in data:
        item = clean(item)
        if validata(item):
            result.append(item)
    return result
print(process_data(["  Hello ", " ", "  World  "])) #['hello', 'world']

#闭包
#每次调用 make_power，内层函数 power 都会"记住"当时的 exp。
def make_power(exp):
    def power(base):
        return base ** exp
    return power
square = make_power(2)
print(square(3))
print(square(4))





