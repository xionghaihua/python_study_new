#读sheet文件

from openpyxl import load_workbook
workbook = load_workbook("p1.xlsx")
#sheet相关操作
#获取sheet的所有名称
print(f"所有工资表:{workbook.sheetnames}")

#选择指定的sheet，通过名字选举,我们还可以基于索引位置选择sheet，workbook.worksheets[0]
ws = workbook['数据导出']
#读取单元格数据
# 读取单个单元格
print(f"A1: {ws['A1'].value}") #序号
print(f"B2: {ws.cell(row=2, column=2).value}") #武沛齐

#读取指定区域的数据
for row in ws.iter_rows(min_row=1,max_row=3,min_col=1,max_col=3,values_only=True):
    print(row)
#读取整行
for row in ws.iter_rows(min_row=1,max_row=5,values_only=True):
    print(row)
#读取整列
for col in ws.iter_cols(min_col=1,max_col=3,values_only=True):
    print(col)

#遍历整个工资表
# 获取最大行数和列数
print(f"最大行数: {ws.max_row}")
print(f"最大列数: {ws.max_column}")
for row in ws.iter_rows(values_only=True):
    print(row)
for i,row in enumerate(ws.iter_rows(values_only=True)):
    print(f"行{i}:{row}")

#读取标头
headers = next(ws.iter_rows(min_row=1,max_row=1,values_only=True))
print(headers)
# 从第二行开始读取数据（跳过表头）
for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)

#获取单元格的属性
cell = ws['A1']
print(f"字体:{cell.font.name}")
print(f"字号: {cell.font.size}")
print(f"加粗: {cell.font.bold}")

# 遍历所有工作表
for sheet_name in workbook.sheetnames:
    ws = workbook[sheet_name]
    print(f"\n工作表: {sheet_name}")
    print(f"数据行数: {ws.max_row}")

    # 读取前5行
    for row in list(ws.iter_rows(values_only=True))[:5]:
        print(row)

#获取合并单元格信息
ws1 = workbook['Sheet2']
for merged in ws1.merged_cells.ranges:
    print(f"合并区域:{merged}")




#按列名读取数据
ws = workbook['数据导出']
header = next(ws.iter_rows(min_row=1,max_row=1,values_only=True))
print(header)
data = []
for row in ws.iter_rows(min_row=2,values_only=True):
    data.append(dict(zip(header,row)))
for record in data:
    if record.get('学生姓名') == '李娜':
        print(f"找到: {record}")

"""
打开文件: load_workbook("p1.xlsx")
获取工作表: wb["Sheet1]
获取单元格: ws["A1"].value  ws.cell(row,col).value
遍历行: ws.iter_row(values_only=True)
遍历列： ws.iter_cols(values_only=True)
获取维度: ws.max_row,ws.max_column
获取标头: next(ws.iter_rows(min_row=1,max_row=1,values_only=True))
"""

