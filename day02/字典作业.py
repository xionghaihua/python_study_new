#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
def print_highlight(text,color=Colors.GREEN):
    print(f"{color}{text}{Colors.RESET}")

while True:
    username = input("请输入用户名:").strip()
    if username.upper() == "Q":
        break
    password = input("请输入密码:").strip()
    try:
        salary = float(input("请输入您的工资（余额）：¥"))
        if salary <= 0:
            print_highlight("工资不能为负数，请重新输入！", Colors.RED)
            continue
        break
    except ValueError:
        print_highlight("请输入有效的数字!",Colors.RED)

balance = salary
print_highlight(f"\n{username}，您的余额为：¥{balance}\n", Colors.GREEN)

products = [
    {"id": 1, "name": "iPhone 15", "price": 6999},
    {"id": 2, "name": "MacBook Pro", "price": 14999},
    {"id": 3, "name": "AirPods Pro", "price": 1899},
    {"id": 4, "name": "iPad Air", "price": 4799},
    {"id": 5, "name": "Apple Watch", "price": 2999},
    {"id": 6, "name": "键盘", "price": 999},
    {"id": 7, "name": "鼠标", "price": 699},
    {"id": 8, "name": "显示器", "price": 3499},
]
cart = []
while True:
    print_highlight("="*50,Colors.GREEN)
    print_highlight("商品列表",Colors.GREEN)
    print_highlight("="*50,Colors.GREEN)
    print(f"{Colors.BOLD}{'编号':<6}{'商品名':<15}{'价格':>10}{Colors.RESET}")
    print("-" * 50)
    for p in products:
        print(f"{p['id']:<6}{p['name']:<15}¥{p['price']:>8}")
    print("-" * 50)
    print_highlight(f"\n当前余额：¥{balance}", Colors.GREEN)
    print("\n输入商品编号购买，输入 'q' 退出结账")
    choice = input("请选择:").strip().lower()
    if choice.upper() == "Q":
        break

    #购买商品
    try:
        product_id = int(choice)
        for p in products:
            if p['id'] == product_id:
                product = p
                break
        if product is None:
            print_highlight("无效商品编号",Colors.RED)
            continue
        if product['price'] > balance:
              print_highlight(f"余额不足！商品价格 ¥{product['price']}，您的余额  ¥{balance}", Colors.RED)
              continue
        balance -= product['price']
        cart.append(product)

        print_highlight(f"✓ {product['name']} 已加入购物车，花费¥{product['price']}", Colors.GREEN)
        print_highlight(f"剩余余额：¥{balance}", Colors.GREEN)

    except ValueError:
        print_highlight("请输入有效的商品编号！", Colors.RED)
        continue
print_highlight("\n" + "=" * 50, Colors.GREEN)
print_highlight("购物清单", Colors.GREEN)
print_highlight("=" * 50, Colors.GREEN)
if cart:
    total_spent = 0
    for item in cart:
        print(f"{item['name']} - ¥{item['price']}")
        total_spent += item['price']

    print_highlight("-" * 50, Colors.GREEN)
    print_highlight(f"总消费：¥{total_spent}", Colors.YELLOW)
    print_highlight(f"剩余余额：¥{balance}", Colors.GREEN)
else:
    print_highlight("未购买任何商品", Colors.YELLOW)
    print_highlight(f"剩余余额：¥{balance}", Colors.GREEN)

print_highlight("=" * 50, Colors.GREEN)
