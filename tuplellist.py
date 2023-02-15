data = (12,3,2,4,5,6,7,8,9,10)
datalist = list(data)
datalist.pop(0)
datalist.pop()
data = tuple(datalist)

print(data)