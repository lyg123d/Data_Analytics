import pandas as pd

data = [100, 200, 300]
index = ['월', '화', '수']

sr = pd.Series(data, index)
print(sr.mean())
print(sr.sum())
print(sr.value_counts())