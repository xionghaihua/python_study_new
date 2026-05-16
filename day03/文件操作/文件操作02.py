#读操作
#read 读所有
#read(n) n 标识字节，字符
#readline 读一行数据
#readlines 读数据，放列表

#读取文件不知道有多少行，按行读取
file = open('./info.txt','rt',encoding='utf-8')
for line in file:
    print(line.strip())
file.close()

with open("./info1.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)  # 一次性读取全部内容为字符串

#读取指定字节数
with open("./info1.txt", "r", encoding="utf-8") as f:
    content = f.read(10)  # 只读前 10 个字符
    print(content)
    content2 = f.read(10)  # 继续读接下来的 10 个字符
    print(content2)
print("---------------------------")
with open("./info1.txt",'r',encoding='utf-8') as f:
    chunk_size = 1024
    while True:
        content = f.read(chunk_size)
        if not content:
            break
        print(content,end="")

print("---------------------------")
#读取一行
with open("./info1.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    print(line)  # 包含行尾的 \n


#逐行读取文件
print("---------------------------")
with open("./info1.txt", "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())
print("---------------------------")
with open("./info1.txt", "r", encoding="utf-8") as f:
    for line in f:  # 自动逐行迭代
        print(line.strip())
print("---------------------------")

#统计文件行数
def count_lines(filename):
    count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            count += 1
    return count
lines = count_lines("./info1.txt")
print(lines)
print("---------------------------")

#读取配置文件
def read_config(filename):
    config = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line and "=" in line.strip():
                key, value = line.split("=",1)
                config[key.strip()] = value.strip()
        return config
config = read_config("./config.txt")
print(config)
print("---------------------------")
with open("./info1.txt", "r", encoding="utf-8") as f_in,\
    open("./info1_bak.txt", "w", encoding="utf-8") as f_out:
    for line in f_in:
        if line.strip():
            f_out.write(line)
