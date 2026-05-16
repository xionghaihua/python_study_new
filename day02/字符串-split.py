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
