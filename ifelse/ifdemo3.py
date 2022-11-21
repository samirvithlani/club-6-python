age = int(input("enter age: "))

if age>=18:
    print("You are eligible to vote")
    if age>=21:
        print("You are eligible to marriage")
    else:
        print("You are not eligible to marriage")    
else:
    print("you are not eligible to vote")
    if age>=5:
        print("you are eligible to study")
            
