import pandas as pd

list =["ram","shyam","mohan","sohan","gita","sita","rita","nita","mita"]

ser = pd.Series(list)
print(ser)


users = {'ram':100,'shyam':200,'mohan':300}

ser = pd.Series(users)
print(ser)

ser = pd.Series(100,index=[1,2,3,4,5,6,7,8,9])
print(ser)

ser = pd.Series(range(20,31))
print(ser)