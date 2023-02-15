no = 1635
temp = no
sum=0
l = len(str(no))

while no!=0:
    rem = no%10
    sum = sum + rem**l
    no = no//10

if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")    
    
