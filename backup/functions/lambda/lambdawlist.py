
def evn(arg):
    for x in range(1,6):
        yield x*arg


env_list =[lambda arg = x : arg *10 for x in range(1,6)]
for i in env_list:
    print(i())
    





