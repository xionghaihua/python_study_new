name = "alex"
print("我叫%s" %name)
#%s 字符串占位符
#%d 整型占位符
#%f 浮点
age = 18
print("我叫%s,今天%d岁" %(name,age))


# %(name)s  %{"name":"alex"}



#format

# 2. 关键字参数
print("姓名：{name}, 年龄：{age}".format(name="李四", age=30))

person = {"name": "赵六", "age": 35}
print("姓名：{0[name]}, 年龄：{0[age]}".format(person))

products = [
    {"name": "笔记本电脑", "price": 5999, "stock": 15},
    {"name": "鼠标", "price": 89, "stock": 120},
]

print("{:-^40}".format("商品清单"))
print("{:<15} {:>10} {:>10}".format("商品名称", "价格", "库存"))
for p in products:
    print("{:<15} {:>10.2f} {:>10}".format(p["name"], p["price"], p["stock"]))


#理解and和or
#and: 遇假者假，全真都为真
#or: 遇真者真，全假都为假
#假值 (Falsy)：False, 0, "", [], {}, None, ()
#真值 (Truthy)：除假值外的所有值

#and，如果第一个为真，结果为第2个值，否则结果为第一个值
print(5 and 3)  #3
print(0 and 3)  #0
print("" and "hello")  #“”

#or，如果第一个为真，结果为第一个值，否则为第二个值
print(5 or 3)  #5
print(0 or 3) #3


