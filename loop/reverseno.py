no = int(input("enter no"))
temp = no

#897    798
sum =0
while no!=0:
    #rem = 897 % 10 = 7
    #rem = 89 % 10 = 9
    #rem = 8 % 10 = 8
    rem = no % 10
    #0 = 0 * 10 + 7 = 7
    #7 = 7 * 10 + 9 = 79
    #79 = 79 * 10 + 8 = 798
    sum =sum * 10 + rem
    #897 = 897 // 10 = 89
    #89 = 89 // 10 = 8
    #8 = 8 // 10 = 0
    no = no // 10


print("reverse no",sum)    

if temp == sum:
    print("palindrome")
else:
    print("not palindrome")
