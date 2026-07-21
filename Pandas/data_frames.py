import pandas as pd

# Method 1: Empty data frames
df = pd.DataFrame()
print(df)


#Method 2 :  Create the Data frame with single dimention list

data = [11,22,33,44,55] # 1*5
df = pd.DataFrame(data) # Series - 1 D
print(df)


# Method 3: Create data frame with multiple dimentional list (list of list) with header
data = [
          ['Alex',10],
          ['Bob',12],
          ['Clarke',13]
        ] # 3*2
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)


# Method 4: with dtype as an argument

data = [['Alex',10],
        ['Bob',12],
        ['Clarke',13]]

df = pd.DataFrame(data, columns=['Name','Age'])
df['Age'] = df['Age'].astype(float)

print(df)
print(df.dtypes)



# Method 5: Create data frame from DICT of series

d = {'one' : pd.Series([1, 2, 3],
      index=['a', 'b', 'c']),
     'two' : pd.Series([88, 2, 3, 4],
      index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df) # fouth raw in first coulmn have value NaN because first Dict have only 3 values so when we are merging both series at Dict the fourth value will be NaN
#print((df[['one','two']]))  # column name -> table
print((df['one'])) # individual column
#print(df.iloc[0]['two'])
#print(df.iat[0,0])
# print(df.at[0,'two'])
print(df['one'].values[2]) # 0 1 2 ...


# Method 6 : create data frames with list of dict and manual index
data = [
        {'a': 1, 'b': 2},
        {'a': 5, 'b': 10, 'c': 20}
        ]
df = pd.DataFrame(data, index=['first', 'second'])
print(df)
