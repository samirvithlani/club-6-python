#keyword argument function...

def test(a):
    print(a)

test(100)    

# def userData(username,email):
#     print("Username is ",username)
#     print("Email is ",email)
#     return username +" "+email

# data = userData("sachin","sachin@gmail.com")
# print(data)
def userData(username,email):
    print("Username is ",username)
    print("Email is ",email)
    return username +" "+email

#keyword argument function
data = userData(username ="sachin",email="sachin@gmail.com")
print(data)


    