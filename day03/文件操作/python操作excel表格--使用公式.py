from openpyxl import Workbook
from openpyxl.styles import PatternFill,Font,Alignment,Border,Side

wb = Workbook()
ws = wb.active


title_font = Font(name='微软雅黑', size=16, bold=True, color='FFFFFF')
title_fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
title_align = Alignment(horizontal='center', vertical='center')

header_font = Font(name='宋体', size=12, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='5B9BD5', end_color='5B9BD5', fill_type='solid')
header_border = Border(
      left=Side(style='thin'),
      right=Side(style='thin'),
      top=Side(style='thin'),
      bottom=Side(style='thin')
)
# 数据样式
data_border = Border(
      left=Side(style='thin'),
      right=Side(style='thin'),
      top=Side(style='thin'),
      bottom=Side(style='thin')
)
#单元格合并
ws.merge_cells("A1:F1")
#解除合并 ws.unmerge_cells("A1:E1")
ws['A1'].value = '工作表'
ws['A1'].font = title_font
ws['A1'].fill = title_fill
ws['A1'].alignment = title_align

# 设置表头
headers = ['员工编号', '姓名', '部门', '基本工资',"学分","等级"]
for col,header in enumerate(headers,start=1):
    cell = ws.cell(row=2,column=col,value=header)
    cell.font = header_font
    cell.fill = header_fill
    cell.border = header_border
    cell.alignment = Alignment(horizontal='center', vertical='center')

reference_data = [
      ['E001', '张三', '技术部', 8000,65],
      ['E002', '李四', '销售部', 6000,92],
      ['E003', '王五', '财务部', 7000,85],
      ['E004', '赵六', '技术部', 8500,74],
      ['E005', '钱七', '销售部', 5500,55],
]
for row_idx,row_data in enumerate(reference_data,start=3):
    for col_idx,value in enumerate(row_data,start=1):
        cell = ws.cell(row=row_idx,column=col_idx,value=value)
        cell.border = data_border
        cell.alignment = Alignment(horizontal='center', vertical='center')

#查询区域
ws['G1'] = '查询编号'
ws['H1'] = '姓名'
ws['I1'] = '部门'
ws['J1'] = '工资'
ws['G2'] = 'E003'

ws['H2'] = '=VLOOKUP(G2, A2:D6, 2, FALSE)'   # 查找姓名
ws['I2'] = '=VLOOKUP(G2, A2:D6, 3, FALSE)'   # 查找部门
ws['J2'] = '=VLOOKUP(G2, A2:D6, 4, FALSE)'   # 查找工资

ws['G3'] = 'E004'
ws['H3'] = '=VLOOKUP(G3, A2:D6, 2, FALSE)'
ws['I3'] = '=VLOOKUP(G3, A2:D6, 3, FALSE)'
ws['J3'] = '=VLOOKUP(G3, A2:D6, 4, FALSE)'


#总计数据
"""
# 使用公式（以 = 开头）
  ws['D1'] = '=SUM(A1:C1)'      # 求和
  ws['E1'] = '=AVERAGE(A1:C1)'  # 平均值
  ws['F1'] = '=MAX(A1:C1)'      # 最大值
  ws['G1'] = '=MIN(A1:C1)'      # 最小值
  ws['H1'] = '=COUNT(A1:C1)'    # 计数
"""

ws['C8'].value = "合计"
ws['D8'] = "=SUM(D3:D7)"
ws['C8'].alignment = Alignment(horizontal='center', vertical='center')
ws['D8'].alignment = Alignment(horizontal='center', vertical='center')

# ws['F2'].value = "等级"
# ws['F2'].alignment = Alignment(horizontal='center', vertical='center')


# IF 条件公式 - for循环版本
for i in range(3, 8):  # 从第2行到第6行
    ws[f'F{i}'] = f'=IF(E{i}>=90,"优秀",IF(E{i}>=80,"良好",IF(E{i}>=60,"及格","不及格")))'
wb.save('./p4.xlsx')

"""
┌───────────┬────────────────────────────────┬───────────────────┐
  │   类别    │              公式              │       说明        │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ 求和      │ =SUM(A1:A10)                   │ 求和              │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ 平均值    │ =AVERAGE(A1:A10)               │ 平均值            │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ 计数      │ =COUNT(A1:A10)                 │ 数字计数          │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ 条件求和  │ =SUMIF(A1:A10, ">100")         │ 条件求和          │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ 条件计数  │ =COUNTIF(A1:A10, "合格")       │ 条件计数          │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ 最大/最小 │ =MAX(A1:A10) / =MIN(A1:A10)    │ 最大/最小值       │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ IF        │ =IF(A1>60, "及格", "不及格")   │ 条件判断          │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ VLOOKUP   │ =VLOOKUP(A1, B1:C10, 2, FALSE) │ 垂直查找          │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ 连接      │ =A1&B1 或 =CONCAT(A1,B1)       │ 文本连接          │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ 截取      │ =LEFT(A1,3)                    │ 左侧截取          │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ 日期      │ =TODAY()                       │ 今日日期          │
  ├───────────┼────────────────────────────────┼───────────────────┤
  │ 四舍五入  │ =ROUND(A1, 2)                  │ 四舍五入到2位小数 
"""
