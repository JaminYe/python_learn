"""
# 大小写互换
print('Test'.swapcase())
# 字符串长度
print(len('test'))
# 是否存在字符串
print('test'.find('e',3))
# 是否存在字符
print('test'.index('s'))
# 是否以字符串开始
print("TEST".startswith("T"))
# 判断字符串是否以指定字符串开始
print("test".endswith('t'))
# 判断字符串中字母是否全是小写
print("t1est".islower())
# 判断字符串中的字母是否全是大写
print('test1'.isupper())
# 判断字符串是否全都以字母类型组成
print('test'.isalpha())
# 判断字符串是否全都以数字或字符串组成
print(s1.isalnum())
s="你好,我是xx,我今年x岁,我上x年级"
print(s.split(',',1))
s1="你好,我是xx,\n我今年x岁,\n我上x年级\n"
print(s.splitlines())
s2="-"
list_l=["ceshi","ceshi2","ceshi3","ceshi4"]
s2=s2.join(list_l)
print(s2)
s="1.22222"
print(s.zfill(10))
s1="   ceshi     "
print(s1.center(10,'*'))
print(s1)
print(s1.strip())
print(s1.replace('c','ss'))

# 要替换的字符串
s='12345'
# 替换成的字符串
s1='qwert'
# 删除的字符串
s2="test"
# 创建映射表
trantab1= str.maketrans(s,s1,s2)
test="test123456789"
print(test.translate(trantab1))
"""
"""
class Person(object):
    def __init__(self, name,age):
        self.name,self.age=name,age
        def __str__(self):
            return "this person is {self.name},age is {self.age} old".format(self=self)


print(str(Person('aa',12)))

# 填充
print( '{:>8}'.format('111'))
# 精度
print('{:.2f}'.format(12.119111111111111111111))

# 进制转换 b,d,o,x,二进制,十进制,八进制,十六进制
print('{:b}'.format(10))
# 千位分隔符
print('{:,}'.format(21312312312312321))
a=1,'123',True
print(id(a))
b='123','21312','123412'
a,b=b,a
print(id(a))
c=['1','2','3','4','5','6']
print(id(c))
d=['12',True,123]
c,d=d,c
print(id(c))
a[0]=100
"""
"""
tuple1=11,12,13
tuple2=12,13,14
set1={tuple1,tuple2}
set2={11,12,143}
# print(set1)
# for x,y,z in set1:
    # print(x,y,z)
set3={x for x in set2 if(x>11) }
print(set2)
"""
'''
set1={1,2}
set2={1,2,3}
print( set1.issubset(set2))
print(set2.issuperset(set1))
set3=frozenset(set1)
for x in set3:
    print(x)
'''
'''
dict1={'1':1,'2':2,'3':3}
dict2=dict({'1':1,'2':2,'3':3})
for x in dict1:
    print(x)
dict4=dict([('1',1),('2',2),(3,3)])
for x,y in dict4.items():
    print('{0}:{1}'.format(x,y))
print(dict4.items())
print(type(dict4.keys()))
print(dict4.values())
print(dict4.get('7'))
print(dict4.pop('1'))
'''
'''
dict1={'1':1,'2':2,'3':3}
dict1.setdefault('5',5)
list1=['1','8','9']
dict2=dict1.fromkeys(list1,1)
for x,y in dict1.items():
    print(x,y)
# print(str(dict2))
print('----------------------------')
dict1.update(dict2)

for x,y in dict1.items():
    print(x,y)
'''
'''
import copy
list1=["test",30,['c++','java','python']]
list2=copy.deepcopy(list1)
print(list1)
print( id(list1))
print([id(x) for x in list1])
print("-------------------------------")
print(list2)
print(id(list2))
print([id(x) for x in list2])
print('修改后'.center(20,'-'))
list1[0]='测试'
list1[1]=30000000000
list1[2][2]='c#'
print(list1)
print( id(list1))
print([id(x) for x in list1])
print("-------------------------------")
print(list2)
print(id(list2))
print([id(x) for x in list2])
'''
"""
def test(a,*b):
    '''
    打印aaa
    sadasdasdas
    '''
    print(a,b)
test(1,2222,33333)
"""
"""
def factorial(n):
    if(n==1):
        return 1
    return n*factorial(n-1)
print(factorial(10))

def test2():
    global a
    a=12

test2()
print(a)
"""
"""
# 文件的基本操作
str1=open("D:\cn.bat",mode='r').read()
print(str1)
"""
'''编码
str2="test"
print(type(str2))
a=str2.encode('utf-8')
print(type(a))
print(a.decode('utf-8'))
'''
''''文件读写
import os
os.chdir('d:/')
file=open('dcnc.bat');
print(file.read())
file=open('dcnc.bat',mode='a+');
file.write('ceshi')
file=open('dcnc.bat',mode='r');
print(file.read())
'''
