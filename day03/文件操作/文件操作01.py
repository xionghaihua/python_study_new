#读文件

#读文本文件
file_object = open('./info.txt','rt')
data = file_object.read()
file_object.close()
print(data)


#判断路径是否存在
import  os
if os.path.exists('./info.txt'):
    with open('./info.txt','rt') as f:
        data = f.read()
        print(data)


#写文件
#wb
file_object = open('./info1.txt',mode='wb')
file_object.write("hello".encode('utf-8'))
file_object.close()

#wt
file_object = open('./info2.txt',mode='wt')
file_object.write("hello")
file_object.close()

#文件打开模式
"""

只写：w，wt，wb
存在：清空再写
不存在：创建在写

只读: r,rt,rb
存在：读
不存在：报错

只写: a,at,ab
尾部追加

读写：
r+,rb+，rt+,可读可写,光标在起始位置
"""

#r+,rb+，rt+,可读可写,光标在起始位置
"""
file_object = open("./info.txt","rt+")
file_object.read() #读取光标起始位置到结束
file_object.write("\n你好")
file_object.close()
"""

#w+,wt+,wb+ 默认光标位置，永远都是起始位置

#a+，at+，ab+ 默认光标在文件的最后

#移动光标  seek(3)







