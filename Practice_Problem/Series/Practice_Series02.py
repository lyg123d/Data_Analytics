import pandas as pd

list_data= [10, 20, 30, 40, 50]
sr = pd.Series(list_data, index=['가', '나', '다', '라', '마'])


print(sr)

#방법2
dict_data = {'가' : 10, '나' : 20, '다' : 30, '라' : 40, '마' : 50}
sr2 = pd.Series(dict_data)

print(sr2)