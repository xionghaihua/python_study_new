#基本语法
def add(a,b):
    return a+b
def calc(fn,a,b):
    return fn(a,b)
result = calc(add,5,6)
print(result)
print("------------------")


def make_multiplier(n):
    def multiplier(x):
        return x * n  # 记住了外层的 n
    return multiplier

double = make_multiplier(2)
print(double(5))


def make_logger(level):
    def log(msg):
        print(f"[{level}] {msg}]")
    return log

info = make_logger("INFO")
info("启动完成")



