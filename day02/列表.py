#列表定义
#是一个有序且可变的容器，在里面可以存放多个不同类型的元素

user_list = ["alex","apple","orange"]
data_list = [1,"text",True,"宝强"]
print(data_list,user_list)

#列表是可变的
user_list = []
user_list.append("铁锤")
user_list.append(1)
print(user_list)

#可变：列表
#不可变: 字符串，布尔，整型

#列表的独有功能
#追加
"""
names = []
while True:
    name = input(">>>请输入姓名，Q/q退出: ").strip()
    if name.lower() == "q":
        break
    names.append(name)
print(f"收集的姓名：{names}") 
"""


events = []
for i in range(1,21):
    if i%2 == 0:
        events.append(i)
print(events)


class Logger:
    def __init__(self):
        self.logs = []
    def info(self,message):
        self.logs.append(message)
    def error(self,message):
        self.logs.append(message)
    def warning(self,message):
        self.logs.append(message)
    def show_logs(self):
        for log in self.logs:
            print(log)
logger = Logger()
logger.info("系统启动")
logger.info("用户登录")
logger.warning("内存使用率高")
logger.error("数据库连接失败")
logger.show_logs()


#购物车功能
cart = []
def add_item(name,price,quantity=1):
    """添加商品到购物车"""
    item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    cart.append(item)
def show_cart():
    if not cart:
        print("购物车为空")
        return
    total = 0
    print("\n=== 购物车 ===")
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{item['name']}: ¥{item['price']} x {item['quantity']} = ¥{subtotal}")
    print(f"总计:¥{total}")
add_item("笔记本电脑", 5999)
add_item("鼠标", 89, 2)
add_item("键盘", 299)
show_cart()


#读取文件并按行存储
def read_file_lines(filename):
    lines=[]
    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

# 解析 CSV 文件
  def parse_csv(filename):
      rows = []
      with open(filename,'r',encoding='utf-8') as f:
          for line in f:
              row = line.strip().split(',')
              rows.append(row)
      return rows