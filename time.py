import time

# temp = time.asctime(time.localtime(time.time()))
temp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
temp = temp.replace(" ", "_")
# print(type(time.asctime(time.localtime(time.time()))))

print(temp)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
