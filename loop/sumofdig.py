#123 1 + 2 + 3  =6

no = int(input("enter no"))
sum=0
count =0
#123 true
#12 true
#1 true
#0 false
while no!=0:
    
    count+=1
    #rem = 123 % 10 = 3
    #rem = 12 % 10 = 2
    #rem = 1 % 10 = 1
    rem = no %10
    #0 = 0 + 3 = 3
    #3 = 3 + 2 = 5
    #5 = 5 + 1 = 6
    sum = sum + rem
    #123 = 123 // 10 = 12
    #12 = 12 // 10 = 1
    #1 = 1 // 10 = 0
    no = no // 10

print("sum of digits",sum)
print("count of digits",count)