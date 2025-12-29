import pandas as pd

data = [100, 200, 300]
index = ['월', '화', '수']

sr = pd.Series(data, index)
sr.loc['목'] = 400
print(sr.drop('수'))
sr.loc['목'] = 900
print(sr)