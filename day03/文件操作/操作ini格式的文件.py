import configparser
config = configparser.ConfigParser()
config.read("my.ini",encoding="utf-8")
ret = config.sections()
#获取所有节点
#print(ret)  #['mysqld', 'mysqld_safe', 'client']

#获取节点下所有的jianzhi
for key,value in config.items("mysqld"):
    print(key,value)
#获取某个节点下键的值
value = config.get("mysqld","collation-server")
print(value)

#其他功能
#判断是否存在这个节点
v1 = config.has_section("mysqld")
print(v1)  #True

#添加节点,和数据
if not config.has_section("group"):
    config.add_section("group")
config.set("group","name","peter")
config.write(open("my.ini",mode="w",encoding="utf-8")) #写到文件

#删除
config.remove_section("client")
config.write(open("my.ini",mode="w",encoding="utf-8"))

config.remove_option("group","name")
config.write(open("my.ini",mode="w",encoding="utf-8"))