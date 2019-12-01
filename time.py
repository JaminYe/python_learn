import time
import calendar
# 时间戳
print(time.time())
# 本地时间
print(time.localtime())
# 格式化时间
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

#2020的日历
print(calendar.calendar(theyear=2020))
# 2019年11月的日历
print(calendar.month(theyear=2019,themonth=11))
# 2019年11月天数
print(calendar.monthlen(2019,11))
# 2019年11月周二的天数
print(calendar.weekday(2019,11,2))
