#解析xml
import xml.etree.ElementTree as ET
#解析xml文件
tree = ET.parse('my.xml')
#获取根节点标签
root = tree.getroot()
print(f"根节点:{root.tag}")

#如果xml通过网络
"""
content=""
root = ET.XML(content)
"""

#查找标签
"""
#遍历所有子节点
for child in root:
    print(f"标签:{child.tag},属性:{child.attrib}")
    for node in child:
        print(node.tag,node.attrib,node.text)

#获取某个标签,如果有多个，输出第一个,findall找所有
country_object = root.find("country")
print(country_object.tag,country_object.attrib)
gdppc_object = country_object.find("gdppc")
print(gdppc_object.text)


#找到所有year的标签，获取值
for child in root.iter("year"):
    print(child.text)
    
"""


#修改标签
rank = root.find('country').find("rank")
print(rank.text)
#修改内容
rank.text = "999"  #字符串类型
#添加属性
rank.set("update","2020-11-11")
print(rank.text,rank.attrib)
#写入文件
tree = ET.ElementTree(root)
tree.write("my.xml")

#删除节点
root.remove(root.find("country"))
tree = ET.ElementTree(root)
tree.write("my.xml")

#构建一个xml文件，添加





