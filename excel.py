import xlrd
'''
excel数据输出
'''
workbook=xlrd.open_workbook('d:/students.xlsx')
sheet1=workbook.sheets()[0]
yunwenlist=[]
shuxuelist=[]
yingyulist=[]
for value in sheet1.col_values(1):
    if type(value)==float:
        yunwenlist.append(value)
for value in sheet1.col_values(2):
    if type(value)==float:
        shuxuelist.append(value)
for value in sheet1.col_values(3):
    if type(value)==float:
        yingyulist.append(value)
def sumList(list_):
    listSum=0
    for i in range(len(list_)):
        listSum+=list_[i]
    return round(listSum/len(list_),2)
print('语文平均分:',sumList(yunwenlist))
print('数学平均分:',sumList(shuxuelist))
print('英语平均分:',sumList(yingyulist))
