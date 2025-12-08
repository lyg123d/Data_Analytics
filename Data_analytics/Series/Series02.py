import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True] # 리스트라 딕셔너리 키처럼 인덱스로 변환될 값 없음 따라서 정수형 위치 인덱스(0, 1, 2)가 자동으로 지정
sr = pd.Series(list_data)
print(sr)

idx = sr.index #인덱스 배열은 idx에 저장
val = sr.values # 데이터 값 배열은 val에 저장
print(idx)
print('\n')
print(val)