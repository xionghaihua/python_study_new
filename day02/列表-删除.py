"""
remove() - 按值删除
pop() - 按索引删除并返回
del - 按索引或切片删除
"""
nums = [1, 2, 3, 4, 5, 6]
nums = [n for n in nums if n % 2 != 0]
print(nums)  # [1, 3, 5]


cart = ["手机", "电脑", "耳机", "手机", "充电器"]
if '手机' in cart:
    cart.remove('手机')
print(cart)


#pop
"""
user_queue = []
while True:
    name = input(">>>北京-上海火车票，购买请输入姓名(q/Q退出):").strip()
    if name.upper() == "Q":
        break
    user_queue.append(name)
ticket_count = 3
for i in range(ticket_count):
    username = user_queue.pop(i)
    message = "恭喜{},购买火车票成功".format(username)
    print(message)
failed_user = ".".join(user_queue)
failed_message = "非常抱歉，票已售完，以下几位用户请选择其他方式，名单:{}".format(failed_user)
print(failed_message)
"""


