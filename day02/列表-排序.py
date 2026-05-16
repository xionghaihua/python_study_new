#升序排序
nums = [5, 2, 9, 1, 7]
nums.sort()
print(nums)  # [1, 2, 5, 7, 9]

#降序排序
nums = [5, 2, 9, 1, 7]
nums.sort(reverse=True)
print(nums)  # [9, 7, 5, 2, 1]

#不修改原列表
nums = [5, 2, 9, 1, 7]
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 2, 5, 7, 9]
print(nums)

#字符串按字母排序
names = ["Charlie", "Alice", "David", "Bob"]
names.sort()
print(names) # ['Alice', 'Bob', 'Charlie', 'David']


#按学生成绩排序
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
]
students.sort(key=lambda x: x["score"])
print(students)

#按元组第二个元素排序
data = [("苹果", 5), ("香蕉", 2), ("橙子", 8)]
data.sort(key=lambda x: x[1])
print(data)  # [('香蕉', 2), ('苹果', 5), ('橙子', 8)]

#先按年龄，再按姓名
persons = [
    ("张三", 25, "北京"),
    ("李四", 30, "上海"),
    ("王五", 25, "广州"),
    ("赵六", 30, "深圳"),
]
#先按年龄升序，年龄相同按姓名升序
persons.sort(key=lambda x: (x[1],x[0]))
print(persons) #[('张三', 25, '北京'), ('王五', 25, '广州'), ('李四', 30, '上海'), ('赵六', 30, '深圳')]


#ord
data = "王宝强"
data_list = []
for char in data:
    v1 = ord(char)
    data_list.append(v1)
print(data_list) #[29579, 23453, 24378]

#商品按价格排序
products = [
    {"name": "手机", "price": 2999},
    {"name": "耳机", "price": 199},
    {"name": "电脑", "price": 5999},
    {"name": "平板", "price": 1999},
]

# 价格从低到高
products.sort(key=lambda x: x["price"])
for p in products:
    print(f"{p['name']}: ¥{p['price']}")

#成绩排名
scores = [
    ("张三", 85, 90, 78),
    ("李四", 92, 88, 95),
    ("王五", 78, 85, 80),
]

# 按总分降序
scores.sort(key=lambda x: sum(x[1:]), reverse=True)
for rank, (name, *s) in enumerate(scores, 1):
    print(f"第{rank}名：{name}, 总分：{sum(s)}")

