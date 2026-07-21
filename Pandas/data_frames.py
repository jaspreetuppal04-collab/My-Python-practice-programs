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

