import pandas as pd

X = pd.read_csv('data.csv', header=None)

X.head()

X.info()


# converts to numpy ndarray
M = X.as_matrix()

# Numpy -> X[0] = 0th row
# Pandas-> X[0] = column named 0
print( X[0])
# pandas Dataframes for 2d object
# pandas Series for 1d object

# 0th row
print( X.iloc[0] )
# OR
print( X.ix[0] )


# column 0 and 2
print( X[[0, 2]] )

# colum 0 < 5
print( X[ X[0] < 5] )
