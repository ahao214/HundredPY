import time
import datetime

print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d'))
print(time.strftime('%Y-%m-%d %H-%M-%S'))

print(datetime.datetime.now())
# 获取当前时间十分钟后的时间
newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)

# 获取某段时间，几天后的时间
oneday = datetime.datetime(2020, 5, 1)
newdate = datetime.timedelta(days=10)
print(oneday + newdate)



