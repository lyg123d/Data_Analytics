import pandas as pd

#DataFrame함수는 2차원 배열이고 행과 열로 구성되어 있다
#DataFrame의 열은 각각 시리즈 개체이다
#딕셔너리의 키(k)는 딕셔너리의 이름이 되고 딕셔너리의 값(v)는 시리즈 배열로 변환되어 데이터프레임의 열이 됨
#dataframe(data,index,columns)양식임

#열이름을 key로 하고 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
dict_data = {'c0' : [1, 2, 3], 'c1' : [4, 5, 6], 'c2' : [7, 8, 9], 'c3' : [10, 11, 12], 'c4' : [13, 14, 15]}
df = pd.DataFrame(dict_data)

print(type(df))
print('\n')
print(df)