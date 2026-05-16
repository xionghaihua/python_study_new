#100以内的所有数字之和
total=0
num = 1
while num < 100:
    total = total + num
    num = num + 1
print(total)


#break，while循环中遇到break，就会立刻终止
"""
print("开始登录")
while True:
    username = input(">>>请输入用户名:").strip()
    passwd = input(">>>请输入密码:").strip()
    if username == "alex" and passwd == "123456":
        print("登录成功")
        break
    else:
        print("登录失败")

print("结束")
"""

#continue 在循环中用于结束本次循环，开启下一次循环
"""
print("开始")
i = 1
while i < 101:
    if i == 7:
        i = i+1
        continue
    print(i)
    i = i + 1
print("结束")
"""
#一旦遇到break，就结束整个循环，遇到continue结束当前循环

#while...else
#只有while的条件不成立了，else才会执行，如果while被break异常退出，else里面的代码就不会执行

"""
while 条件:
   代码
else:
   代码
"""


#字符串格式化
"""
1、使用%字符串格式化
2、基于format字符串格式化
3.基于f字符串格式化
"""








