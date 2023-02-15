no = 123
temp = no
sum=0
l = len(str(no))

while no!=0:
    #123 % 10 3
    #12 % 10 2
    #1 % 10 1
    rem = no%10
    #0 = 0 +3 sum =3
    #3 = 3 * 10 + 2 sum = 32
    #32 = 32 * 10 + 1 sum = 321
    sum = (sum * 10) + rem
    #12
    #1
    no = no//10

print(sum)
    
