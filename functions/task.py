def data(*args):
    print("Your hobbies are: ")
    for i in args:
        print(i)


flag =1

while True:
    hobby = input("Enter your hobby: ")
    flag = input("Do you want to enter more hobbies? (y/n): ")
    if flag == 'n':
        break
    else :
        print("Enter more hobbies")
        data(hobby)
    
        