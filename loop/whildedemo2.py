no = int(input("enterno "))

# no /10  12 /10 = 1.
# no % 10  12 % 10 = 2
#123 = 3    
#123 // 10 = 12
#12 // 10 = 1
#1 // 10 = 0
count=0
while no != 0:
    count+=1
    no = no // 10
    
print("no of digits ",count)    
    
    