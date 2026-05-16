from concurrent.futures.thread import ThreadPoolExecutor
POOL = ThreadPoolExecutor(max_workers=10)
import requests

video_list = [
    ("东北F4模仿秀.mp4","https://aweme.snss")
]
def task(url):
    res = requests.get(
        url = url,
        headers = {
            "user-agent": ""
        }
    )
#下载完成后，多线程内部需要执行的函数
def outer(filename):
    def done(arg):
        content = arg.result()
        with open(filename, "a") as f:
            f.write(content)
    return done
for item in video_list:
    #去线程池取一个人，执行任务
    future = POOL.submit(task,url=item[1])
    future.add_done_callback(outer(item[0])) #当执行完成后，自动执行其他操作