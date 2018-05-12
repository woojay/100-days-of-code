import pandas as pd

x1 = pd.read_csv('file1.csv')
x2 = pd.read_csv('file2.csv')

m = pd.merge( x1, x2, on='user_id')

#OR

x1.merge(x2, on='user_id')
