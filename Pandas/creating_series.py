# Method 1

import pandas as pd

s = pd.Series() # Empty series 
print(s) # data in list, data - type


#Method 2 We did not pass the index still you can see index value in first column in output

s = pd.Series(['a','b','c','a']) # index -> easily access
print(s)

# Method 3 : we can create the series with numpy ndarray
import numpy as np
s = pd.Series(np.array(['a','b','c','d']))
print(s)