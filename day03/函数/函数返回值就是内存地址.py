def modify(lst):
    lst.append(4)
    return lst  # 返回的还是原对象的引用


data = [1, 2, 3]
result = modify(data)
print(id(data),id(result))
print(id(data) == id(result))

print("====================================")

