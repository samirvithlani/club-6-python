#[] () {}
#data = () #tuple
#data =[] #list
#data ={} #dictionary
#how to declare empty set
data = {12,22,34,56,77,88,99,100}

data.update([100,200,300])
#data.add(400)
#data.remove(1000)
#data.discard(1000)
x = data.pop()
print("removing....",x)

print("data",data)
ins = data.intersection({100,200,300,3})
print("ins",ins)
#data.intersection_update({100,200,300,3})
print("data",data)

#diff1 = data.difference({100,200,300})
#data.difference_update({100,200,300})
#print("diff1",diff1)
#print("data",data)

flag = data.issubset({100,200,300,12,22,34,56,77,88,99,100,9,0})
print("flag",flag)

uni =data.union({100,200,300})
print("uni",uni)


