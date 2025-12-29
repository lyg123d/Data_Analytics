import pandas as pd

data = [100, 200, 300]
index = ['월', '화', '수']

sr = pd.Series(data, index)

print(sr.loc['월']) # 월요일의 데이터 값 출력
print(sr.iloc[2]) # 수요일 값 출력 
print(sr.iloc[-1])
print(sr[[0, 1]])
print(sr.iloc[[1, 2]])
print(sr.iloc[0:2])
print(sr.loc[['월', '화']])
print(sr.loc['월':'화'])