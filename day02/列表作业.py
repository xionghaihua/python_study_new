"""
li = ["alex","Wusir","ritian",'barry','wupeiqi']

print(len(li))
li.append("seven")
li.insert(1,"tony")
data = [1,'a',3,4,'heart']
li.extend(data)
print(li)

s = "qwert"
for item in s:
    li.append(item)
print(li)

#删除列表中barry
if 'barry' in li:
    li.remove('barry')
#删除第二个元素
ele = li.pop(1)
print(ele,li)

del li[2:4]
print(li)
"""

