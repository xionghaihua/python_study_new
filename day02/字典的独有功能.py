#keys(), values(), items()
person = {"name": "张三", "age": 25, "city": "北京"}

print(person.keys())  # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['张三', 25, '北京'])
print(person.items())  #dict_items([('name', '张三'), ('age', 25), ('city', '北京')])

keys_list = list(person.keys())
print(keys_list)

#键不存在，默认返回None
person = {"name": "张三", "age": 25}
age = person.setdefault("age",30)
print(person)
#键不存在时添加
job = person.setdefault("job","工程师")
print(person) #{'name': '张三', 'age': 25, 'job': '工程师'}


if "age" in person.keys():
    print("age是person的键")

#fromkeys() 创建字典
keys = ["a","b","c"]
d = dict.fromkeys(keys,0)
print(d) #{'a': 0, 'b': 0, 'c': 0}

#字典推导式
nums = [1,2,3,4,5]
squares = {x:x**2 for x in nums}
print(squares)

#统计词频
text = "python is awesome python is great"
words = text.split()
print(words)
word_count = {}
for word in words:
    word_count[word] = word_count.get(word,0) + 1
print(word_count) #{'python': 2, 'is': 2, 'awesome': 1, 'great': 1}

#学生成绩管理
students = {
      "001": {"name": "张三", "score": 85},
      "002": {"name": "李四", "score": 92},
      "003": {"name": "王五", "score": 78},
}
print(students["001"]["name"])
total = sum(s["score"] for s in students.values())
print(total)

#keys,values,items
#移除指定键值对
age = person.pop("age")
print(age) #25
print(person) #{'name': '张三', 'job': '工程师'}

header = ["股票名称","当前价","涨跌额"]
stock_dict = {
    "SH601778": ["中国晶科",'6.29','+1.92'],
    "SH601566": ["吉贝尔", '26.29', '+6.92'],
    "SH601268": ["华腾气体", '88.29', '+11.92']
}

for key,value in stock_dict.items():
    #print(key,value)
    text_list = []
    for index in range(len(value)):
        text = "{}:{}".format(header[index],value[index])
        text_list.append(text)
    data = "、".join(text_list)
    result = "{}.{}".format(key,data)
    print(result)

