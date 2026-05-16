matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])  # [1, 2, 3]
print(matrix[1][2])  # 6


#
students = [
    ["张三", 85, 90, 78],
    ["李四", 92, 88, 95],
    ["王五", 78, 85, 80],
]

for student in students:
    name = student[0]
    scores = student[1:]
    avg = sum(scores) / len(scores)
    print(f"{name}: 平均分 {avg:.1f}")


#生成用户列表
#[['alex', '123'], ['peter', '123']]
user_list = []
while True:
    username=input("请输入用户名:").strip()
    if username.upper() == "Q":
        break
    password=input("请输入密码:").strip()
    data = [username, password]
    user_list.append(data)
print(user_list)