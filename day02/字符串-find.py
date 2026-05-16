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