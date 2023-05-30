import pandas as pd
import numpy as np

dict ={"f":[100,200,np.nan,77],"s":[7,20,30,56],'t':[100,np.nan,56,78]}
df = pd.DataFrame(dict) 
#creating dataframe using nukk
#df  = df.isnull()
#print(df)

#df = df.fillna(0)
#print(df)
#print(df)
#df = df.dropna(axis=1)
#print(df)



for i in df.itertuples():
    for x in i:
        print(x)
    
    print()

