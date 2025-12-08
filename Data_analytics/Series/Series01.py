import pandas as pd

#Seires: 순차적으로 나열된 1차원 배열로 인덱스(index)는 데이터 값(value)과 일대일로 대응
#Series(data,index, dtype)순으로 입력
dict_data = {'a' : 1, 'b' : 2, 'c' : 3} # 딕셔너리형

sr = pd.Series(dict_data) #시리즈 클래스가 됌
print(type(sr)) 
print(sr)
