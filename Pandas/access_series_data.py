import pandas as pd

# Method 1: by index value
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e']) # a -> 0, b->1,...

#retrieve the first element
print(s)
print(s['a']) # 0 : a -> 1

# Method 2: fetch multiple value from the data... means First 3 values
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e']) # 0 1 2 3 4
print((s[:3])) # in argument start : end # start(0) to end-1

# Method 3 index value ith negative index
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print((s['a']))
#print((s[-3:])) # in argument start : end

# Method 4 : retrieve value using lable index
s = pd.Series([1,2,3,4,5],index = [2,2,2,3,3]) # 0,1,2
print((s[2])) 