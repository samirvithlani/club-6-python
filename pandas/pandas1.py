import pandas as pd
import numpy as np

ser =pd.Series()
print(ser)

data = np.array(['a','b','c','d','f','g','h','i','j'])

#ser = pd.Series(data)
ser = pd.Series(data,index=[100,101,102,103,111,105,106,107,108])
print(ser)