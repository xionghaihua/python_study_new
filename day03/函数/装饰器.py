def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第 {i+1} 次失败: {e}")
            print("全部重试完成")
        return wrapper
    return decorator

@retry(3)
def fetch_data(url):
    import requests
    return requests.get(url, timeout=2)
fetch_data("https://unstable-api.example.com")

print("=============================================")

#计数器
#无参数的装饰器
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(1000000)  # slow_sum 耗时: 0.0xxxs

print("=============================================")

#有参数的装饰器
import functools
def before_after(before_msg, after_msg):
    def decorator(fn):
        @functools.wraps(fn)  #保留原函数的名称和描述
        def wrapper(*args, **kwargs):
            print(before_msg)
            result = fn(*args, **kwargs)
            print(after_msg)
            return result
        return wrapper
    return decorator

@before_after("开启事务", "提交事务")
def save_data():
    print("保存数据...")

