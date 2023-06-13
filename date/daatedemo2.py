import time

#current time...
#print(time(11, 34, 56))

mills = int(round(time.time() * 1000))
print(mills)

strtime = time.strftime("%H:%M:%S:", time.localtime())
print(strtime)
ctrtime = time.ctime()
print(ctrtime)
