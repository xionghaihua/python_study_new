#字典是无序，键不重复且元素只能是键值对的可变的容器

#字典中的键: 必须是可哈希的，字符串，元组，bool，int
#字典中的值：可以是任何类型

#字典创建
person = dict(name="李四", age=30, city="上海")
print(person)


#访问元素
#通过键访问
person = {"name": "张三", "age": 25, "city": "北京"}
print(person["name"])  # 张三
print(person["age"])  # 25

#访问不存在的键会报错
# print(person["job"])  # KeyError: 'job'

#使用 get() 安全访问
print(person.get("city"))

#修改和添加
person["age"] = 26
person["job"] = "工程师"
print(person)


#使用 update() 批量更新
person.update({"age": 26, "city": "北京", "job": "工程师"})
print(person)

#删除元素
#pop() 并返回值
age = person.pop("age")
print(age)  # 26

#popitem() 删除最后一对
k, v = person.popitem()
print(k,v)


#遍历字典
for key in person:
    print(f"{key}: {person.get(key)}")

#
info = {"k1":"v1","k2":"v2","k3":"v3"}
key_list=[]
value_list=[]
for key,value in info.items():
    key_list.append(key)
    value_list.append(value)
print(key_list,value_list)

#
result = {}
text = "k1:1|k2:2|k3:3"
data_list = text.split("|")
#print(data_list)
for item in data_list:
    key,value = item.split(":")
    result[key] = int(value.strip())
print(result) #{'k1': '1', 'k2': '2', 'k3': '3'}

#
result = {}
li = [11,22,33,44,55,66,77,88,90]
for item in li:
    if item >66:
        if "k1" in result:
            result["k1"].append(item)
        else:
            result["k1"] = [item]
    elif item == 66:
        pass
    else:
        if "k2" in result:
            result["k2"].append(item)
        else:
            result["k2"] = [item]
print(result)


#
goods = [
    {"name": "iPhone 15", "price": 6999},
    {"name": "MacBook Pro", "price": 14999},
    {"name": "AirPods Pro", "price": 1899},
    {"name": "iPad Air", "price": 4799},
    {"name": "Apple Watch", "price": 2999},
    {"name": "键盘", "price": 999},
    {"name": "鼠标", "price": 699},
    {"name": "显示器", "price": 3499},
]
for index in range(len(goods)):
    item = goods[index]
    print(index+1,item["name"],item["price"])

while True:
    num = input("请输入要选择的商品序号:").strip()
    if num.upper() == "Q":
        break
    if not num.isdecimal():
        print("用户输入的序号错误")
        continue
    num = int(num)
    if num <0 or num >len(goods):
        print("序号范围选择错误")
        continue
    target_index = num -1
    choice_item = goods[target_index]
    print(choice_item["name"],choice_item["price"])






