#str,需要用英文的引号把字符串引起来
print("我是alex")


#字符串相加

print("hello " + "world")


#两个字符串也可以进行比较

"""
其他所有类型转换成布尔类型时，除了空字符串，0，其他都为true  
"""


#字符串独有功能
#1. 大小写转换
s = "hello WORLD"
print(s.lower()) #转小写
print(s.upper()) #转大写  #不改变原来的

#2、startswith是不是以某个开头，endswith是不是以什么结尾
files = ["app.py", "data.txt", "image.png", "doc.pdf"]
for f in files:
    if f.startswith((".py", ".txt")):
        print(f"{f} 是文本文件")

for f in files:
    if f.endswith(".py"):
        print(f"{f} 是 Python 文件")
    elif f.endswith((".txt", ".md")):
        print(f"{f} 是文本文件")
    elif f.endswith((".jpg", ".png")):
        print(f"{f} 是图片文件")

def parse_command(cmd):
    cmd = cmd.strip().lower()
    if cmd.startswith("/"):
        if cmd.endswith("help"):
            return "显示详细信息"
        elif cmd.endswith("version"):
            return "显示版本1.0"
        elif cmd.endswith("list"):
            return "列出所有项目"
        else:
            return f"未知命令:{cmd}"
    else:
        return "请输入以/开头的的命令"
print(parse_command("  /help  "))   # 显示帮助信息
print(parse_command("/version"))       # 显示版本
print(parse_command("/list"))       # 列出所有项目

#参数可以是元组，实现多值判断
url = "https://example.com"
print(url.startswith(("http://", "https://", "ftp://")))  # True

# 批量检查文件类型
files = ["a.py", "b.txt", "c.md", "d.jpg"]
# 统计 Python 文件数量
py_files = [f for f in files if f.endswith(".py")]
print(f"Python 文件：{py_files}")  # ['a.py']


#字符串查找替换
#replace() - 替换子字符串
#案例 1：敏感词过滤
def filter_sensitive_words(text,sensitive_words):
    """
    过滤敏感词
    :param text: 原始文本
    :param sensitive_words: 敏感词列表
    :return:  过滤后的文本
    """
    result = text
    for word in sensitive_words:
        result = result.replace(word,'*'*len(word))
    return result
text = "这个产品很好，但是客服态度很差"
sensitive = ["差", "垃圾"]
print(filter_sensitive_words(text, sensitive))

#查找并替换特定格式内容

def replace_phone_number(text,replacement="***"):
    import re
    pattern = r"1[3-9]\d{9}"
    return re.sub(pattern, replacement, text)

text = "联系电话：13812345678，备用：19987654321"
print(replace_phone_number(text))

#字符串查找
s = "hello world, hello python"
def find_all(text,target):
    positions = []
    start = 0
    while True:
        pos = text.find(target, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

print(find_all(s, "hello"))

#字符串切割split
# 默认按空白字符切割（空格、制表符、换行符等）
s1 = "hello world python"
print(s1.split())  # ['hello', 'world', 'python']
# 指定分隔符
s2 = "apple,banana,orange"
print(s2.split(","))  # ['apple', 'banana', 'orange']

#maxsplit参数 - 限制切割次数
s = "apple,banana,orange,grape"
# 只切割 1 次
print(s.split(",", 1))  # ['apple', 'banana,orange,grape']

url = "https://example.com?name=tom&age=20&city=beijing"
query_string = url.split("?")[1]
params = query_string.split("&")
for param in params:
    key, value = param.split("=")
    print(f"{key}: {value}")

#解析时间
time_str = "12:30:45"
hours, minutes, seconds = time_str.split(":")
print(f"{hours}时 {minutes}分 {seconds}秒")  # 12 时 30 分 45 秒

# 使用 re 模块按多种分隔符切割
import re
text = "apple,banana;orange|grape"
# 按 , ; | 切割
result = re.split(r"[,;|]", text)
print(result)  # ['apple', 'banana', 'orange', 'grape']


def parse_log_line(line):
    """解析日志行：时间 级别 消息"""
    parts = line.split(" ", 2)  # 只切割 2 次
    if len(parts) >= 3:
        return {"time": parts[0], "level": parts[1], "message": parts[2]}
    return None

log = "2024-01-15 10:30:45 ERROR 数据库连接失败"
print(parse_log_line(log))

#字符串拼接join
fruits = ["apple", "banana", "orange"]
print(", ".join(fruits))  # "apple, banana, orange"


def list_to_csv_row(data):
    return ",".join(str(item) for item in data)


row = ["张三", 25, "北京", "工程师"]
print(list_to_csv_row(row))  # "张三，25，北京，工程师"


def generate_sql_in(column, values):
    """生成 SQL IN 子句"""
    values_str = ", ".join(f"'{v}'" for v in values)
    return f"{column} IN ({values_str})"

print(generate_sql_in("id", [1, 2, 3, 5]))

# 编码解码
s_encoded = "你好".encode("utf-8")
print(s_encoded)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(s_encoded.decode("utf-8"))  # "你好"


message = "hello "
index = 0
while index < len(message):
    value = message[index]
    print(value)
    index += 1

index = len(message)-1
while index >=0:
    value = message[index]
    print(value)
    index -= 1

def extract_between(text,start_marker,end_marker):
    """提取两个标记之间的内容"""
    start = text.find(start_marker)
    #print(start)
    if start == -1:
        return None
    start += len(start_marker)  #标签start的长度
    #print(start)
    end = text.find(end_marker,start)
    #print(end)
    if end == -1:
        return None
    return text[start:end]

html = "<title>我的网页</title>"
print(extract_between(html, "<title>", "</title>"))  # "我的网页"
text = "用户名：[admin]，权限：[root]"
print(extract_between(text, "[", "]"))


#for循环
message = "明天天气晴朗"
for i in range(0,len(message)):
    if message[i] == "气":
        break
    value = message[i]
    print(value)


#简单url解析
def parse_url(url):
    """简单解析url"""
    result ={"protocol": "", "domain": "", "path": ""}
    #查找协议
    proto_end = url.find("://")
    print(proto_end)  #5

    if proto_end != -1:
        result["protocol"] = url[:proto_end]
        #print(result["protocol"])  #https
        url = url[proto_end+3:]  #www.example.com/home/index.html
    #查找路径
    path_start = url.find("/")
    print(path_start)   #15
    if path_start != -1:
        result["domain"] = url[:path_start]
        result["path"] = url[path_start:]
    else:
        result["domain"] = url
        result["path"] = "/"
    return result
print(parse_url("https://www.example.com/home/index.html"))

#
def exact_error_info(log_info):
    error_start = log_info.find("ERROR")
    if error_start == -1:
        return None

    msg_start = error_start + len("ERROR")
    message = log_info[msg_start:].strip()
    return {"level": "ERROR", "message": message}
log1 = "2024-01-15 10:30:45 ERROR 数据库连接失败"
log2 = "2024-01-15 10:30:46 INFO 系统启动成功"
print(exact_error_info(log1))
print(exact_error_info(log2))


v1 = 123
v2 = 456
data = bin(v1)[2:].zfill(16) + bin(v2)[2:].zfill(16)
result = int(data, 2)
print(result)



ip = "10.3.9.12"
data_list = []
num_list = ip.split(".")
for num in num_list:
    item = bin(int(num))[2:].zfill(8)
    data_list.append(item)
print(data_list)
#翻转[::-1]
reverse_data = "".join(data_list)[::-1]
result = int(reverse_data, 2)
print(result)

car_list = ['鲁A32444',"沪B22342","京B9823N","京A75232"]
info = {}
for item in car_list:
    city = item[0]
    #字典get方法，不存在，设置为0
    num = info.get(city,0)
    info[city] = num + 1
print(info)

text = """id,name,age,phone,job
1,alex,22,13651054242,IT
2,wusir,23,13304320422,Teacher"""
data_list = text.split("\n")
head_list = data_list[0].split(",") #标头
#print(data_list)
info = []
#索引位置对应
for index in range(1,len(data_list)):
    item = {}
    row = data_list[index]
    row_item_list = row.split(",")
    for i in range(len(row_item_list)):
        item[head_list[i]] = row_item_list[i]
    info.append(item)
print(info)

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        text = "{}*{}={}".format(j,i,i*j)
        print(text,end=" ")
    print("")

