
#370
no = int(input("enter no"))
temp = no
rem=0 
sum =0

#370!=0 true
#37!=0 true
#3!=0 true
#0!=0 false
while no!=0:
    
    #rem = 370 % 10 = 0
    #rem = 37 % 10 = 7 
    rem = no % 10
    #sum = 0 +0 * 0 = 0
    #sum= 0 + 7 * 7 * 7 = 343
    #343 = 343 + 3 * 3 * 3 = 370
    sum = sum + rem ** 3
    #370 = 370//10 37
    #37 = 37 / 10 3
    #3 = 3 //10 0
    no = no // 10


if temp == sum:
    print("armstrong")
else:
    print("not armstrong")    