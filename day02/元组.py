#有一个有序且不可变的容器，在里面可以存放多个不同类型的元素

v3 = (True,123,"ALex",[11,22,33])
v3[3].append(44)
print(v3) #(True, 123, 'ALex', [11, 22, 33, 44])

#循环
for item in v3:
    print(item)


#