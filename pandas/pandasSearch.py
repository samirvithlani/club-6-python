import pandas as pd

dict = {"Name":["samir","raj","parth","san jay"],"Age":[20,21,22,23],"City":["surat","ahmedabad","baroda","rajkot"],"salary":[10000,20000,30000,40000]}

df = pd.DataFrame(dict)
#print(df)
#df = df[df["Age"]>22]
#df = df[(df["Age"]>=21) & (df["salary"]>=30000)]
# Name =start with s
df = df[df["Name"].str.startswith("s")]
#df = df[df["Name"]== "samir"]

print(df)