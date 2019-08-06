from datetime import datetime, timedelta, timezone
import re

now = datetime.now() 
print(now)
print(type(now))

dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)
print(dt.timestamp())

t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print(now.strftime('%a, %b %d %H:%M'))

print(now + timedelta(hours=10))

print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)

dt = now.replace(tzinfo=tz_utc_8)
print(dt)

# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


def to_timestamp(dt_str, tz_str):
    l = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tznum = re.match(r'^UTC([\+\-](\d)+):00$',tz_str)
    tz = timezone(timedelta(hours=int(tznum.group(1))))
    return l.replace(tzinfo=tz).timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')