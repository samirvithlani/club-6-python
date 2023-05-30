import pandas as pd

data = pd.read_csv("D:\\royal\\club6-python\\pandas\\data.csv")
#print(data)

#first = data.loc[0]
#print(first)
first = data.loc[0:3]
print(first)