import pandas as pd

users = {'Name': ['Bob', 'Jessica', 'Mary', 'John', 'Mel'],'salary': [70000, 80000, 120000, 90000, 95000],
         'age': [25, 30, 35, 40, 45],'city': ['Boston', 'Dallas', 'Chicago', 'Atlanta', 'Anaheim']}
df = pd.DataFrame(users)
#print(df)

#print(df[['Name', 'city']])
#print(df[2:4])
print(df[2:4][['Name', 'city']])