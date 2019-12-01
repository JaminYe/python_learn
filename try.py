'''异常处理
def test(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print('0不可除')
    except TypeError:
        print('类型错误')
    finally:
        print('结束')
print(test(4,1))
print(test('111','222'))
'''
'''迭代器
from collections.abc import Iterable
print(isinstance('test',Iterable))
strItr=iter('test')
print(next(strItr))
list1 =["1","2",3,4,5]
listItr=iter(list1)
print(next(listItr))
'''

list_1=[x*x for x in range(100000)]
# print(list_1)
list_2=(x*x for x in range(3))
print(list_2)
# print(next(list_2))
# print(next(list_2))
# print(next(list_2))
# for x in list_2:
    # print(x)
def print_a(max):
    i=0
    while(i<max):
        i+=1
        yield i
a=print_a(10)
print(a)
print(type(a))
print(next(a))
print(a.__next__())
def print_b(max):
    i=0
    while i<max:
        i=i+1
        args=yield i
        print('测试'+args)
b=print_b(100)
print(b.__next__())
print(b.send('cxe'))
