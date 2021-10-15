import time

# 可以做日期运算，并且windows支持到2038年
ticks = time.time()
print("当前时间戳为:", ticks)

# 时间元组
localtime = time.localtime(time.time())
print("元组：本地时间为：", localtime)

# 格式化时间
localtime = time.asctime(time.localtime(time.time()))
print("格式化1：本地时间为：", localtime)

# 格式化成2016-03-20 11:45:39形式
localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("格式化2：本地时间为：", localtime)

# 格式化成Sat Mar 28 22:24:24 2016形式
localtime = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
print("格式化3：本地时间为：", localtime)

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print("格式字符串转化时间戳", a, "→",
      time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
